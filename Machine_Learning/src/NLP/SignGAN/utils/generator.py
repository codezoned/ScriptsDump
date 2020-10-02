import numpy as np
import tensorflow as tf
from .conv_attention import ConvAttn

# '.' added to look outside the directory (else import error)
# We will feed 'z' from outside. If it is inside it'll stay constant and won't be random
class CDCGAN(tf.keras.layers.Layer):
    def __init__(self):
        super(CDCGAN, self).__init__()

        self.dense = tf.keras.layers.Dense(4 * 4 * 4 * 1024)
        #self.layernorm = tf.keras.layers.LayerNormalization()
        #self.leakyrelu = tf.keras.layers.LeakyReLU()

        self.reshape = tf.keras.layers.Reshape((4, 4, 4, 1024))

        # (4, 4, 4, 512)
        self.deconv1 = tf.keras.layers.Conv3DTranspose(filters=512, 
                                                    kernel_size=(3, 3, 3), 
                                                    strides=(1, 1, 1), 
                                                    padding='same', 
                                                    use_bias=False)
        
        self.layernorm1 = tf.keras.layers.LayerNormalization()
        #self.leakyrelu1 = tf.keras.layers.LeakyReLU()
        self.relu1 = tf.keras.layers.Activation('relu')

        # (8, 8, 8, 256)
        self.deconv2 = tf.keras.layers.Conv3DTranspose(filters=256, 
                                                    kernel_size=(3, 3, 3), 
                                                    strides=(2, 2, 2), 
                                                    padding='same', 
                                                    use_bias=False)
        
        self.layernorm2 = tf.keras.layers.LayerNormalization()
        #self.leakyrelu2 = tf.keras.layers.LeakyReLU()
        self.relu2 = tf.keras.layers.Activation('relu')

        # attn -> (32, 8, 8, 128)
        self.conv1 = tf.keras.layers.Conv3D(filters=128, 
                                            kernel_size=(3, 3, 3),
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)
        
        self.attnlayernorm1 = tf.keras.layers.LayerNormalization()
        #self.attnleakyrelu1 = tf.keras.layers.LeakyReLU()
        self.attnrelu1 = tf.keras.layers.Activation('relu')

        # attn -> (16, 8, 8, 256)
        self.conv2 = tf.keras.layers.Conv3D(filters=256, 
                                            kernel_size=(3, 3, 3),
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)

        self.attnlayernorm2 = tf.keras.layers.LayerNormalization()
        #self.attnleakyrelu2 = tf.keras.layers.LeakyReLU()
        self.attnrelu2 = tf.keras.layers.Activation('relu')

        # attn -> (8, 8, 8, 512)
        self.conv3 = tf.keras.layers.Conv3D(filters=512, 
                                            kernel_size=(3, 3, 3),
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)
                    
        self.attnlayernorm3 = tf.keras.layers.LayerNormalization()
        #self.attnleakyrelu3 = tf.keras.layers.LeakyReLU()
        self.attnrelu3 = tf.keras.layers.Activation('relu')
        

        # (8, 16, 16, 128)
        self.deconv3 = tf.keras.layers.Conv3DTranspose(filters=128, 
                                                    kernel_size=(3, 3, 3), 
                                                    strides=(1, 2, 2), 
                                                    padding='same', 
                                                    use_bias=False)
        
        self.layernorm3 = tf.keras.layers.LayerNormalization()
        #self.leakyrelu3 = tf.keras.layers.LeakyReLU()
        self.relu3 = tf.keras.layers.Activation('relu')

        # (16, 32, 32, 64)
        self.deconv4 = tf.keras.layers.Conv3DTranspose(filters=64, 
                                                    kernel_size=(3, 3, 3), 
                                                    strides=(2, 2, 2), 
                                                    padding='same', 
                                                    use_bias=False)
        
        self.layernorm4 = tf.keras.layers.LayerNormalization()
        #self.leakyrelu4 = tf.keras.layers.LeakyReLU()
        self.relu4 = tf.keras.layers.Activation('relu')

        # (16, 64, 64, 32)
        self.deconv5 = tf.keras.layers.Conv3DTranspose(filters=32, 
                                                    kernel_size=(3, 3, 3), 
                                                    strides=(1, 2, 2), 
                                                    padding='same', 
                                                    use_bias=False)
        
        self.layernorm5 = tf.keras.layers.LayerNormalization()
        #self.leakyrelu5 = tf.keras.layers.LeakyReLU()
        self.relu5 = tf.keras.layers.Activation('relu')

        # (16, 64, 64, 3)
        self.deconv6 = tf.keras.layers.Conv3DTranspose(filters=3, 
                                                    kernel_size=(3, 3, 3), 
                                                    strides=(1, 1, 1), 
                                                    padding='same', 
                                                    use_bias=False,  
                                                    activation='relu')   # values > 0


    def call(self, z, conv_attn_output):
        assert len(z.shape) == 2    # (1, 100)

        # same z repeated for all the clips
        z = tf.repeat(z, repeats=conv_attn_output.shape[0], axis=0)

        z = self.dense(z)
        #z = self.layernorm(z)
        #z = self.leakyrelu(z)

        z = self.reshape(z)

        # Upscaling z
        z = self.deconv1(z)
        z = self.layernorm1(z)
        z = self.relu1(z)

        z = self.deconv2(z)
        z = self.layernorm2(z)
        z = self.relu2(z)      # (32, 8, 8, 8, 256)

        # Attn out -> (32, 64, 8, 8, 64)
        # Downscale Attention output -> (32, 8, 8, 8, 64)
        conv_attn_output = self.conv1(conv_attn_output)
        conv_attn_output = self.attnlayernorm1(conv_attn_output)
        conv_attn_output = self.attnlayernorm1(conv_attn_output)

        conv_attn_output = self.conv2(conv_attn_output)
        conv_attn_output = self.attnlayernorm2(conv_attn_output)
        conv_attn_output = self.attnlayernorm2(conv_attn_output)

        conv_attn_output = self.conv3(conv_attn_output)
        conv_attn_output = self.attnlayernorm3(conv_attn_output)
        conv_attn_output = self.attnlayernorm3(conv_attn_output)
        
        # Concat condition (downscaled attention output) across channel dimension
        z = tf.concat([z, conv_attn_output], axis=-1)

        # upconv to produce 40 clips with 40 as bs, thus generating the whole video
        z = self.deconv3(z)
        z = self.layernorm3(z)
        z = self.relu3(z)

        z = self.deconv4(z)
        z = self.layernorm4(z)
        z = self.relu4(z)
        
        z = self.deconv5(z)
        z = self.layernorm5(z)
        z = self.relu5(z)
        
        z = self.deconv6(z)

        return z
        

class Generator(tf.keras.Model):
    def __init__(self, num_attention_blocks=4, out_channels=64):
        super(Generator, self).__init__()

        self.attention = ConvAttn(num_attention_blocks, out_channels)
        self.cdcgan = CDCGAN()

    def call(self, x, bert_embeddings, z):
        x = self.attention(x, bert_embeddings)
        x = self.cdcgan(z, x)
        #if np.isnan(np.sum(x)) == np.nan:
        #    print('-----CDCGAN-----')

        return x
