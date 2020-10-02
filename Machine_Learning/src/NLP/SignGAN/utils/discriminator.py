import tensorflow as tf
from .errors import MatrixRankError

# Using scheme 2 of Microsoft

# 0 < disc_vals < 1
class VideoDiscriminator(tf.keras.layers.Layer):
    def __init__(self):
        super(VideoDiscriminator, self).__init__()

        self.dense1 = tf.keras.layers.Dense(4 * 4 * 256)

        # Input -> (512, 64, 64, 3)
        # (512, 64, 64, 8)
        self.conv0 = tf.keras.layers.Conv3D(filters=8, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(1, 1, 1), 
                                            padding='same', 
                                            use_bias=False)

        # (256, 64, 64, 16)
        self.conv1 = tf.keras.layers.Conv3D(filters=16, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)

        # (128, 64, 64, 32)
        self.conv2 = tf.keras.layers.Conv3D(filters=32, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)
        
        # (64, 64, 64, 64)
        self.conv3 = tf.keras.layers.Conv3D(filters=64, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)
        
        # (32, 64, 64, 128)
        self.conv4 = tf.keras.layers.Conv3D(filters=128, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)
        
        # (16, 64, 64, 256)
        self.conv5 = tf.keras.layers.Conv3D(filters=256, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 1, 1), 
                                            padding='same', 
                                            use_bias=False)

        # (8, 32, 32, 512)
        self.conv6 = tf.keras.layers.Conv3D(filters=512, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (4, 16, 16, 1024)
        self.conv7 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (2, 8, 8, 1024)
        self.conv8 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (1, 4, 4, 1024)
        self.conv9 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(2, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # After concat
        self.conv10 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(3, 3, 3), 
                                            strides=(1, 1, 1), 
                                            padding='same', 
                                            use_bias=False)


        self.relu = []
        self.batchnorm = []
        for i in range(11):
            self.batchnorm.append(tf.keras.layers.BatchNormalization())
            self.relu.append(tf.keras.layers.Activation('relu'))

        self.flatten = tf.keras.layers.Flatten()

        self.dense2 = tf.keras.layers.Dense(128)

        self.dense3 = tf.keras.layers.Dense(1)#, activation='sigmoid')    # output -> [0, 1]


    def call(self, v, s):   # video and sentence embedding
        # s -> sentence vector
        if len(v.shape) != 5:
            raise MatrixRankError("v must be a Rank 5 Tensor i.e, (batch_size, num_clips * T, H, W, C)")
        if len(s.shape) != 2:
            raise MatrixRankError("s must be a Rank 2 Tensor i.e, (batch_size, dim)")
        
        batch_size, t, h, w, c = v.shape

        # Sentence semantic space
        s = self.dense1(s)
        s = tf.reshape(s, (batch_size, 1, 4, 4, 256))

        # downscale v
        v = self.conv0(v)
        v = self.batchnorm[0](v)
        v = self.relu[0](v)

        v = self.conv1(v)
        v = self.batchnorm[1](v)
        v = self.relu[1](v)

        v = self.conv2(v)
        v = self.batchnorm[2](v)
        v = self.relu[2](v)

        v = self.conv3(v)
        v = self.batchnorm[3](v)
        v = self.relu[3](v)

        v = self.conv4(v)
        v = self.batchnorm[4](v)
        v = self.relu[4](v)

        v = self.conv5(v)
        v = self.batchnorm[5](v)
        v = self.relu[5](v)

        v = self.conv6(v)
        v = self.batchnorm[6](v)
        v = self.relu[6](v)

        v = self.conv7(v)
        v = self.batchnorm[7](v)
        v = self.relu[7](v)

        v = self.conv8(v)
        v = self.batchnorm[8](v)
        v = self.relu[8](v)

        v = self.conv9(v)
        v = self.batchnorm[9](v)
        v = self.relu[9](v)

        # concat with s
        v = tf.concat([v, s], axis=-1)

        v = self.conv10(v)
        v = self.batchnorm[10](v)
        v = self.relu[10](v)

        v = self.flatten(v)
        v = self.dense2(v)
        v = self.dense3(v)

        return v


# 0 < disc_vals < 1
class FrameDiscriminator(tf.keras.layers.Layer):
    def __init__(self):
        super(FrameDiscriminator, self).__init__()

        # 3D conv used instead of 2D, to consider batch size i.e, more than 1 video at a time
        # Time dimension technically not considered because stride is  always = 1 and kernel size along time is always 1, so temporal relation is not taken into account

        self.dense1 = tf.keras.layers.Dense(4 * 4 * 256)

        # (64, 64, 8)
        self.conv0 = tf.keras.layers.Conv3D(filters=8, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 1, 1), 
                                            padding='same', 
                                            use_bias=False)

        # (32, 32, 16)
        self.conv1 = tf.keras.layers.Conv3D(filters=16, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (16, 16, 32)
        self.conv2 = tf.keras.layers.Conv3D(filters=32, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)
        
        # (8, 8, 64)
        self.conv3 = tf.keras.layers.Conv3D(filters=64, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)
        
        # (4, 4, 128)
        self.conv4 = tf.keras.layers.Conv3D(filters=128, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)
        
        # (4, 4, 256)
        self.conv5 = tf.keras.layers.Conv3D(filters=256, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 1, 1), 
                                            padding='same', 
                                            use_bias=False)
        '''
        # (32, 32, 512)
        self.conv6 = tf.keras.layers.Conv3D(filters=512, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (16, 16, 1024)
        self.conv7 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (8, 8, 1024)
        self.conv8 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)

        # (4, 4, 1024)
        self.conv9 = tf.keras.layers.Conv3D(filters=1024, 
                                            kernel_size=(1, 3, 3), 
                                            strides=(1, 2, 2), 
                                            padding='same', 
                                            use_bias=False)
        '''
        
        # After concat (FRAME)
        self.conv_frame = tf.keras.layers.Conv3D(filters=512, 
                                                kernel_size=(1, 3, 3), 
                                                strides=(1, 1, 1), 
                                                padding='same', 
                                                use_bias=False)

        # After concat (MOTION)
        self.conv_motion = tf.keras.layers.Conv3D(filters=512, 
                                                kernel_size=(1, 3, 3), 
                                                strides=(1, 1, 1), 
                                                padding='same', 
                                                use_bias=False)

        
        self.relu = []
        self.batchnorm = []
        for i in range(8):  #12
            self.batchnorm.append(tf.keras.layers.BatchNormalization())
            self.relu.append(tf.keras.layers.Activation('relu'))

        self.frame_flatten = tf.keras.layers.Flatten()

        #self.dense_frame_1 = tf.keras.layers.Dense(128)

        self.dense_frame_2 = tf.keras.layers.Dense(1)#, activation='sigmoid')    # output -> [0, 1]

        self.motion_flatten = tf.keras.layers.Flatten()

        #self.dense_motion_1 = tf.keras.layers.Dense(128)

        self.dense_motion_2 = tf.keras.layers.Dense(1)#, activation='sigmoid')    # output -> [0, 1]


    def call(self, v, s):
        if len(v.shape) != 5:
            raise MatrixRankError("v must be a Rank 5 Tensor i.e, (batch_size, num_clips * T, H, W, C)")
        if len(s.shape) != 2:
            raise MatrixRankError("s must be a Rank 2 Tensor i.e, (batch_size, dim)")

        batch_size, t, h, w, c = v.shape

        # downscale v
        v = self.conv0(v)
        v = self.batchnorm[0](v)
        v = self.relu[0](v)

        v = self.conv1(v)
        v = self.batchnorm[1](v)
        v = self.relu[1](v)

        v = self.conv2(v)
        v = self.batchnorm[2](v)
        v = self.relu[2](v)

        v = self.conv3(v)
        v = self.batchnorm[3](v)
        v = self.relu[3](v)

        v = self.conv4(v)
        v = self.batchnorm[4](v)
        v = self.relu[4](v)

        v = self.conv5(v)
        v = self.batchnorm[5](v)
        v = self.relu[5](v)
        '''
        v = self.conv6(v)
        v = self.leakyrelu[6](v)
        print('7')

        v = self.conv7(v)
        v = self.leakyrelu[7](v)
        print('8')

        v = self.conv8(v)
        v = self.leakyrelu[8](v)
        print('9')
        
        v = self.conv9(v)
        v = self.leakyrelu[9](v)    # common output
        print('10')
        '''
        ## Take this output and work for temporal coherence

        ## Frame
        # Sentence semantic space
        s = self.dense1(s)
        s = tf.reshape(s, (batch_size, 1, 4, 4, 256))
        frame_s = tf.repeat(s, repeats=t, axis=1)   # time axis next to the batch because 't' frames
        # Concat and out
        frame_out = tf.concat([v, frame_s], axis=-1)

        frame_out = self.conv_frame(frame_out)
        frame_out = self.batchnorm[6](frame_out)
        frame_out = self.relu[6](frame_out)
        # output 1 for each frame so reshape to (batch_size * t, h, w, c)
        frame_out = tf.reshape(frame_out, (batch_size * frame_out.shape[1], frame_out.shape[2], frame_out.shape[3], frame_out.shape[4]))

        frame_out = self.frame_flatten(frame_out)   # (bs*t, .., .., ..)
        #frame_out = self.dense_frame_1(frame_out)   # (bs*t, ..)
        frame_out = self.dense_frame_2(frame_out)   # (bs*t,)

        # reshaped to (batch_size, t)
        frame_out = tf.reshape(frame_out, (batch_size, frame_out.shape[0] // batch_size)) # out
        # for each frame of each batch, we get an output
        
        ## Motion
        # Sentence Semantic space
        motion_s = tf.repeat(s, repeats=t-1, axis=1)
        motion_out = tf.subtract(v[:, 1:], v[:, :-1])

        # Concat and out
        motion_out = tf.concat([motion_out, motion_s], axis=-1)

        motion_out = self.conv_motion(motion_out)
        motion_out = self.batchnorm[7](motion_out)
        motion_out = self.relu[7](motion_out)

        # Scheme 2 (no norm)
        motion_out = tf.reshape(motion_out, (batch_size * motion_out.shape[1], motion_out.shape[2], motion_out.shape[3], motion_out.shape[4]))

        motion_out = self.motion_flatten(motion_out)    # (bs*(t-1), .., .., ..)
        #motion_out = self.dense_motion_1(motion_out)    # (bs*(t-1), ..)
        motion_out = self.dense_motion_2(motion_out)    # (bs*(t-1),)

        # (bs, t-1)
        motion_out = tf.reshape(motion_out, (batch_size, motion_out.shape[0] // batch_size)) # out
        
        return frame_out, motion_out


# 0 < disc_vals < 1
class Discriminator(tf.keras.Model):
    def __init__(self):
        super(Discriminator, self).__init__()

        self.video_discriminator = VideoDiscriminator()
        self.frame_discriminator = FrameDiscriminator()

    def call(self, v, s):
        video_disc_out = self.video_discriminator(v, s)
        frame_disc_out, motion_disc_out = self.frame_discriminator(v, s)

        return video_disc_out, frame_disc_out, motion_disc_out

