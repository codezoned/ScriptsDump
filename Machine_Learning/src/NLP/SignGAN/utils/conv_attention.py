import tensorflow as tf
import numpy as np

from .errors import *

@tf.function
def masking(shape, position):
    if position > shape[0]:
        raise PaddingError("padding position exceeds limits. position must be < shape[0]")

    if len(shape) != 4:
        raise MatrixRankError("Shape must be of Rank 4 i.e, (T, H, W, val), val -> H*W or, T*W or, T*H")

    # mask only for time dimension, size -> (t, h*w, h*w)
    '''
    zero = tf.zeros((position, shape[1], shape[2], shape[3]), dtype=tf.float32)
    fill = tf.fill((shape[0]-position, shape[1], shape[2], shape[3]), -np.inf)
    mask = tf.concat([zero, fill], 0)
    '''
    
    return tf.concat([tf.zeros((position, shape[1], shape[2], shape[3]), dtype=tf.float32), 
                    tf.fill((shape[0]-position, shape[1], shape[2], shape[3]), -np.inf)], 0)

    #return mask

@tf.function
def look_ahead_mask(num_mask, shape):
    if shape[0] % num_mask != 0:
        raise DivisionError("Time dimension must be divisible by number of masks")
    if len(shape) != 4:
        raise MatrixRankError("Shape must be of Rank 4 i.e, (T, H, W, val), val -> H*W or, T*W or, T*H")

    mask = tf.expand_dims(masking(shape, 1 * shape[0] // num_mask), 0)
    for mask_pos in range(1, num_mask):    # shape[0] = 500
        mask = tf.concat([mask, tf.expand_dims(masking(shape, (mask_pos+1) * shape[0] // num_mask), 0)], 0)

    return mask     # shape -> (50, T, H, W, C)

@tf.function
def dot_product_attention(q, k, v, mask):
    # Number of columns of q must be equal to number of columns of k
    # i.e the last dimension must be same

    # This if-else block is for self attention and, word embedding attention
    if len(k.shape) == 2:
        k_T = tf.transpose(k)
    else:
        k_T =  tf.transpose(k, perm=[0, 1, 3, 2])    # which axis will be at which place specified
    
    qv_correlations = tf.matmul(q, k_T)
    
    if mask is not None:
        num_clips, qv_1, qv_2, qv_3 = qv_correlations.shape
        '''
        try:
            mask = tf.reshape(mask, (num_clips, qv_1, qv_2, qv_3))
        except:
            raise ValueError("Reshaped Mask does not match 'matmul(Q, K.T)' in shape")
        '''
        qv_correlations += mask
        #print(qv_correlations)

    return tf.matmul(tf.nn.softmax(qv_correlations, axis=0), v)


## Word Frame Attention
# Last dimension of both masked_attention_output and semantic_word_matrix must be same
# 2nd last dimenstion i.e, 1st dimenstion of semantic_word_matrix should equal to H*W of masked-separable-self-attention output because the same mask_t will be used
# that is, we bring both to a common semantic space using conv for frames and dense for embeddings
class Attention(tf.keras.layers.Layer):
    # tf.keras.layers.Dense changes the last dimenstion of n-d matrix
    def __init__(self, channel_dimension=64):
        # downsample to H*W = 64 i.e, H = 8, W = 8, before the attention block.
        # common semantic space = 64, i.e, channel_dimension = 64
        # result after tf.Dense Layer : 1. semantic_word_matrix -> (64, 64)      2. Downsampled masked/repeated video -> (50, 500, 8, 8, 64)

        super(Attention, self).__init__()

        self.channel_dimension = channel_dimension

        # For separable self attention
        self.sep_wq1 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wq1')
        self.sep_wk1 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wk1')
        self.sep_wv1 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wv1')

        self.sep_wq2 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wq2')
        self.sep_wk2 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wk2')
        self.sep_wv2 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wv2')

        self.sep_wq3 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wq3')
        self.sep_wk3 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wk3')
        self.sep_wv3 = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='sep_wv3')

        # For word-frame attention
        self.word_wq = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='word_wq')
        self.word_wk = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='word_wk')
        self.word_wv = tf.keras.layers.Dense(self.channel_dimension, use_bias=False, name='word_wv')

        # batchnorm causes nan because of the padding and masking, so layernorm
        self.layernorm1 = tf.keras.layers.LayerNormalization()
        self.layernorm2 = tf.keras.layers.LayerNormalization()

    '''
    def separable_attention(self, x, mask_t, mask_h, mask_w):
        try:
            num_clips, t, h, w, c = x.shape
        except:
            raise MatrixRankError("x must be of rank 5 i.e, (num_clips, t, h, w, c)")
        
        if len(mask_t.shape) != 5 or len(mask_h.shape) != 5 or len(mask_h.shape) != 5:
            raise MatrixRankError("masks must be of rank 5 i.e, (num_clips, t, h, w, val), where val -> H*W or, T*W or, T*H")
        
        x = tf.reshape(x, (num_clips, t, h*w, c))
        xq, xk, xv = self.sep_wq1(x), self.sep_wk1(x), self.sep_wv1(x)
        x = dot_product_attention(xq, xk ,xv, tf.reshape(mask_t, (num_clips, t, h*w, h*w)))   # self Attention
        #print(x.shape)

        x = tf.reshape(x, (num_clips, h, t*w, c))
        xq, xk, xv = self.sep_wq2(x), self.sep_wk2(x), self.sep_wv2(x)
        x = dot_product_attention(xq, xk ,xv, tf.reshape(mask_h, (num_clips, h, t*w, t*w)))   # self Attention

        x = tf.reshape(x, (num_clips, w, t*h, c))
        xq, xk, xv = self.sep_wq3(x), self.sep_wk3(x), self.sep_wv3(x)
        x = dot_product_attention(xq, xk ,xv, tf.reshape(mask_w, (num_clips, w, t*h, t*h)))   # self Attention
        
        return tf.reshape(x, (num_clips, t, h, w, c))
    '''
    '''
    def separable_attention(self, x, mask_t, mask_h, mask_w, xq_t, xk_t, xv_t, xq_h, xk_h, xv_h, xq_w, xk_w, xv_w):
        try:
            num_clips, t, h, w, c = x.shape
        except:
            raise MatrixRankError("x must be of rank 5 i.e, (num_clips, t, h, w, c)")
        
        if len(mask_t.shape) != 5 or len(mask_h.shape) != 5 or len(mask_h.shape) != 5:
            raise MatrixRankError("masks must be of rank 5 i.e, (num_clips, t, h, w, val), where val -> H*W or, T*W or, T*H")
        
        x = dot_product_attention(xq_t, xk_t ,xv_t, tf.reshape(mask_t, (num_clips, t, h*w, h*w)))   # self Attention

        x = dot_product_attention(xq_h, xk_h ,xv_h, tf.reshape(mask_h, (num_clips, h, t*w, t*w)))   # self Attention

        x = dot_product_attention(xq_w, xk_w ,xv_w, tf.reshape(mask_w, (num_clips, w, t*h, t*h)))   # self Attention
        
        return tf.reshape(x, (num_clips, t, h, w, c))
    '''
    '''
    def word_frame_attention(self, frame_features, bert_embeddings, mask_t):      # only across time
        try:
            num_clips, t, h, w, c = frame_features.shape
        except:
            raise MatrixRankError("frame_features must be of rank 5 i.e, (num_clips, t, h, w, c)")
        
        if len(mask_t.shape) != 5:
            raise MatrixRankError("mask_t must be of rank 5 i.e, (num_clips, t, h, w, val), where val -> H*W or, T*W or, T*H")

        frame_features = tf.reshape(frame_features, (num_clips, t, h*w, c))

        frame_features, bert_embeddings, bert_embeddings = self.word_wq(frame_features), self.word_wk(bert_embeddings), self.word_wv(bert_embeddings)

        frame_features = dot_product_attention(frame_features, bert_embeddings, bert_embeddings, tf.reshape(mask_t, (num_clips, t, h*w, h*w)))

        return tf.reshape(frame_features, (num_clips, t, h, w, c))
    '''

    def call(self, frame_features, bert_embeddings, mask_t, mask_h, mask_w):
        # make sure that q, k, v have gone through tf.expand_dims, because of the batch simension thing
        # for 2nd point above. if q = v that means self attention, hence, q != v
        assert (frame_features.shape[-2] * frame_features.shape[-3]) == bert_embeddings.shape[-2]       # for 2nd point above. if q = v that means self attention, hence, q != v
        # 8*8 == 64
    
        #attn_out = self.separable_attention(frame_features, mask_t, mask_h, mask_w)
        # Separable self-attn
        try:
            num_clips, t, h, w, c = frame_features.shape
        except:
            raise MatrixRankError("frame_features must be of rank 5 i.e, (num_clips, t, h, w, c)")
        
        x = tf.reshape(frame_features, (num_clips, t, h*w, c))
        xq, xk, xv = self.sep_wq1(x), self.sep_wk1(x), self.sep_wv1(x)
        x = dot_product_attention(xq, xk ,xv, tf.reshape(mask_t, (num_clips, t, h*w, h*w)))
        
        x = tf.reshape(x, (num_clips, h, t*w, c))
        xq, xk, xv = self.sep_wq2(x), self.sep_wk2(x), self.sep_wv2(x)
        x = dot_product_attention(xq, xk ,xv, tf.reshape(mask_h, (num_clips, h, t*w, t*w)))

        x = tf.reshape(x, (num_clips, w, t*h, c))
        xq, xk, xv = self.sep_wq3(x), self.sep_wk3(x), self.sep_wv3(x)
        x = dot_product_attention(xq, xk ,xv, tf.reshape(mask_w, (num_clips, w, t*h, t*h)))   # self Attention

        x = tf.reshape(x, (num_clips, t, h, w, c))
        frame_features = self.layernorm1(frame_features + x)

        #attn_out = self.word_frame_attention(frame_features, bert_embeddings, mask_t)
        # Word-frame attention
        x = tf.reshape(frame_features, (num_clips, t, h*w, c))
        x, bert_k, bert_v = self.word_wq(x), self.word_wk(bert_embeddings), self.word_wv(bert_embeddings)
        x = dot_product_attention(x, bert_k, bert_v, tf.reshape(mask_t, (num_clips, t, h*w, h*w)))
        x = tf.reshape(x, (num_clips, t, h, w, c))

        frame_features = self.layernorm2(frame_features + x)

        return frame_features



# use tf.keras.Model to make it a different model
# Can see summary only after passing an input. Simply calling the model won't work
# Gotta pass a sample input to get going
class ConvAttn(tf.keras.layers.Layer):
    def __init__(self, num_attention_blocks=4, out_channels=64):
        super(ConvAttn, self).__init__()

        self.num_attention_blocks = num_attention_blocks
        self.out_channels = out_channels

        # (16, 64, 64, 8)
        self.conv1 = tf.keras.layers.Conv3D(filters=8, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(1, 1, 1), 
                                            padding='same', 
                                            use_bias=False)

        # (8, 32, 32, 16)
        self.conv2 = tf.keras.layers.Conv3D(filters=16, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (4, 16, 16, 32)
        self.conv3 = tf.keras.layers.Conv3D(filters=32, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (2, 8, 8, out_channels)
        self.conv4 = tf.keras.layers.Conv3D(filters=self.out_channels, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # LayerNorm and ReLU
        self.relu = []
        self.layernorm = []
        for i in range(4):
            self.relu.append(tf.keras.layers.Activation('relu'))
            self.layernorm.append(tf.keras.layers.LayerNormalization())

        self.attention = []
        for i in range(self.num_attention_blocks):
            self.attention.append(Attention(self.out_channels))

    def call(self, x, bert_embeddings):
        if len(x.shape) != 5:
            raise MatrixRankError("x was supposed to be a Rank 5 tensor, i.e, (num_clips, T, H, W, C)")
        
        assert self.out_channels == bert_embeddings.shape[-2]

        x = self.conv1(x)
        x = self.layernorm[0](x)
        x = self.relu[0](x)
        #print("Conv1 Out Shape : ", x.shape)

        x = self.conv2(x)
        x = self.layernorm[1](x)
        x = self.relu[1](x)
        #print("Conv2 Out Shape : ", x.shape)

        x = self.conv3(x)
        x = self.layernorm[2](x)
        x = self.relu[2](x)
        #print("Conv3 Out Shape : ", x.shape)
        
        x = self.conv4(x)
        x = self.layernorm[3](x)
        x = self.relu[3](x)
        #print("Conv4 Out Shape : ", x.shape)

        #if np.isnan(np.sum(x)) == np.nan:
        #    print('-----CONV-----')

        num_clips, t, h, w, c = x.shape
        x = tf.reshape(x, (num_clips * t, h, w, c))
        t = num_clips * t

        x = tf.repeat(x, repeats=num_clips, axis=0)
        x = tf.reshape(x, (num_clips, t, h, w, c))

        mask_t = look_ahead_mask(num_clips, (t, h, w, h*w))
        mask_h = look_ahead_mask(num_clips, (t, h, w, t*w))
        mask_w = look_ahead_mask(num_clips, (t, h, w, t*h))

        for i in range(self.num_attention_blocks):
            x = self.attention[i](x, bert_embeddings, mask_t, mask_h, mask_w)
        

        return x
