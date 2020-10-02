import tensorflow as tf
import numpy as np
import glob
import cv2

class Video(object):
    def __init__(self, T = 16, MAX_VIDEO_LENGTH = 640, FRAME_DIM = (64, 64, 3), VIDEO_DIM = (640, 64, 64, 3),
                data_dir = 'phoenix-2014-T.v3/PHOENIX-2014-T-release-v3/PHOENIX-2014-T/features/fullFrame-210x260px/'):
        self.T = T
        self.MAX_VIDEO_LENGTH = MAX_VIDEO_LENGTH
        self.FRAME_DIM = FRAME_DIM
        self.VIDEO_DIM = VIDEO_DIM
        self.data_dir = data_dir

    def get_video(self, set_name, name, resize=True, scale_down=True):
        vid = []
        for frame in glob.glob(self.data_dir + set_name + '/' + name + '/*.png'):
            vid_frame = cv2.imread(frame)
            if resize:
                vid_frame = cv2.resize(vid_frame, (self.FRAME_DIM[0], self.FRAME_DIM[1]))
            if scale_down:
                vid_frame = vid_frame / 255.         # 0 < pixel values < 1, padding = 0
            vid.append(vid_frame)
        return tf.convert_to_tensor(np.array(vid, np.float32))

    def padding(self, video):
        pad_length = self.MAX_VIDEO_LENGTH - video.shape[0]
        pad = tf.zeros((pad_length, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), dtype=tf.float32)
        return tf.concat([video, pad], 0)

    def preprocess_video(self, video):
        start_token = tf.fill((self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), 256./255)       # start token -> 4d array of 0.9
        #print(start_token.shape)
        end_token = tf.fill((self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), 257./255)         # end token -> 4d array of 2.1
        #print(end_token.shape)
        extra_token = tf.fill((self.T - video.shape[0] % self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), 1.)        # padding starts only from the nearest 10th, so until the nearest 10, array of 1's
        #print(extra_token.shape)
        #video = tf.concat([tf.concat([start_token, video], 0), extra_token], 0)
        #video = tf.concat([tf.cast(start_token, tf.float32), tf.cast(video, tf.float32), tf.cast(extra_token, tf.float32), tf.cast(end_token, tf.float32)], 0)
        video = tf.concat([start_token, video, extra_token, end_token], 0)
        #print(video)
        
        #video = np.append(video, end_token, axis=0)
        video = self.padding(video)
        return video
    
    def divide_sequence(self, preprocessed_video):
        return tf.reshape(preprocessed_video, (self.MAX_VIDEO_LENGTH//self.T, self.T, preprocessed_video.shape[1], preprocessed_video.shape[2], preprocessed_video.shape[3]))
        #return np.array(np.array_split(preprocessed_video, self.MAX_VIDEO_LENGTH//self.T, axis=0))

    '''
    # may not be needed
    def padding_mask(self, current_sequence_length):     # so that paddings are not treated as input
        division = current_sequence_length // self.T + 2     # includes start_token so 2
        #print(division)

        mask = np.zeros((division, self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), dtype=np.float)
        mask = np.append(mask, np.ones((self.MAX_VIDEO_LENGTH//self.T - division, self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), dtype=np.float), axis=0)

        return mask

    # may not be needed
    def look_ahead_mask(self):
        mask = np.zeros((1, self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), dtype=np.float)
        mask = np.append(mask, np.ones((49, self.T, self.FRAME_DIM[0], self.FRAME_DIM[1], self.FRAME_DIM[2]), dtype=np.float), axis=0)
        mask = np.expand_dims(mask, axis=0)
        #print(mask.shape)
        for i in range(0, self.MAX_VIDEO_LENGTH - 2 * self.T + 1, self.T):
            mask = np.append(mask, np.expand_dims(self.padding_mask(i), axis=0), axis=0)
        return mask
    '''

'''
def main():
    video_obj = Video()
    video = video_obj.get_video('train', '05January_2010_Tuesday_tagesschau-2664')
    current_sequence_length = video.shape[0]

    video = video_obj.preprocess_video(video)
    print(video.shape)

    video = video_obj.divide_sequence(video)
    print(video.shape)

    pad_mask = video_obj.padding_mask(current_sequence_length)
    print(pad_mask.shape)

    look_mask = video_obj.look_ahead_mask()
    print(look_mask.shape)


if __name__ == '__main__':
    main()
'''
