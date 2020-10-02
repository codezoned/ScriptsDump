import tensorflow as tf
import numpy as np
import glob
import time
import os

from bert_utils import Bert
from utils.video import Video
from utils.conv_attention import *
from utils.generator import *
from utils.discriminator import *
from utils.losses import *

# Optional
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

# Models
bert = Bert()
generator = Generator()
discriminator = Discriminator()

num_clips = 32
T = 16 # let
MAX_VIDEO_LENGTH = 512      # 475 is the longest
FRAME_DIM = (64, 64, 3)
VIDEO_DIM = (512, 64, 64, 3)
data_dir = 'phoenix-2014-T.v3/PHOENIX-2014-T-release-v3/PHOENIX-2014-T/features/fullFrame-210x260px/'
video_obj = Video(T, MAX_VIDEO_LENGTH, FRAME_DIM, VIDEO_DIM, data_dir)

EPOCHS = 10000

# Otimizers
learning_rate = 0.000001
generator_optimizer = tf.keras.optimizers.Adam(learning_rate)
discriminator_optimizer = tf.keras.optimizers.Adam(learning_rate)

# ckpt
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(generator_optimizer=generator_optimizer,
                                 discriminator_optimizer=discriminator_optimizer,
                                 generator=generator,
                                 discriminator=discriminator)

# Takes correct video, wrong video and word embeddings, sentence
# all of this must be preprocessed (padded and stuff)
# Video must be explicitly divided into T frames

def train_step(video_real, video_wrong, text):
    num_clips, t, h, w, c = video_real.shape
    word, sentence = bert([text])
    word, sentence = tf.convert_to_tensor(word), tf.convert_to_tensor(sentence)
    word = tf.squeeze(word)
    z = tf.random.normal(shape=(1, 100))

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        video_fake = generator(video_real, word, z)

        # All frames put together with bs = 1
        video_real = tf.reshape(video_real, (1, num_clips * t, h, w, c))
        video_wrong = tf.reshape(video_wrong, (1, num_clips * t, h, w, c))
        video_fake = tf.reshape(video_fake, (1, num_clips * t, h, w, c))

        # Discriminator out
        disc_video_real, disc_frame_real, disc_motion_real = discriminator(video_real, sentence)
        disc_video_wrong, disc_frame_wrong, disc_motion_wrong = discriminator(video_wrong, sentence)
        disc_video_fake, disc_frame_fake, disc_motion_fake = discriminator(video_fake, sentence)

        # Losses
        total_video_loss = video_loss(disc_video_real, disc_video_wrong, disc_video_fake)
        total_frame_loss = frame_loss(disc_frame_real, disc_frame_wrong, disc_frame_fake)
        total_motion_loss = motion_loss(disc_motion_real, disc_motion_wrong, disc_motion_fake)

        disc_loss = discriminator_loss(total_video_loss, total_frame_loss, total_motion_loss)
        gen_loss = generator_loss(disc_video_fake, disc_frame_fake, disc_motion_fake)

    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
    

def main():
    dataset = open('phoenix-2014-T.v3/PHOENIX-2014-T-release-v3/PHOENIX-2014-T/annotations/manual/PHOENIX-2014-T.train.corpus.csv', encoding='utf-8')
    dataset = dataset.readlines()[1:]

    text_data = [i.split('|')[-1][:-1] for i in dataset]     # [:-1] to remove '\n' at the end
    video_data = [i.split('|')[0] for i in dataset]

    for epoch in range(EPOCHS):
        start = time.time()
        for text, video in zip(text_data, video_data):
            video_real = video_obj.get_video('train', video)
            video_real = video_obj.preprocess_video(video_real)
            video_real = video_obj.divide_sequence(video_real)

            # Random video from dataset as the wrong video
            video_wrong = video_obj.get_video('train', video_data[np.random.randint(0, len(video_data))])
            video_wrong = video_obj.preprocess_video(video_wrong)
            video_wrong = video_obj.divide_sequence(video_wrong)
            
            train_step(video_real, video_wrong, text)

        if (epoch + 1) % 10 == 0:
            checkpoint.save(file_prefix=checkpoint_prefix)
    
        print("Epoch {0} :- Time : {1}".format(epoch + 1, time.time() - start))
        


if __name__ == '__main__':
    main()
