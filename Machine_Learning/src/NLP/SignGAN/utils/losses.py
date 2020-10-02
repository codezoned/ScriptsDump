import tensorflow as tf

# disc_video_real -> Disc out for Real video matching with the sentence [single value]
# disc_video_wrong -> Disc out wrong <sentence, video> pair [single value]
# disc_video_fake -> Disc out for Generated video [single value]
# Mean of whole batch taken

# Use BCE loss. Refer tf2-GANs
bce = tf.keras.losses.BinaryCrossentropy(from_logits=True)

@tf.function
def video_loss(disc_video_real, disc_video_wrong, disc_video_fake):
    return (bce(tf.ones_like(disc_video_real), disc_video_real) + bce(tf.zeros_like(disc_video_wrong), disc_video_wrong) + bce(tf.zeros_like(disc_video_fake), disc_video_fake)) / 3.

# disc_frame_real -> Disc out for Real video frames matching with the sentence [Vector of values for each frame]
# disc_frame_wrong -> Disc out wrong <sentence, video> pair frames [Vector of values for each frame]
# disc_frame_fake -> Disc out for Generated frames [Vector of values for each frame]
@tf.function
def frame_loss(disc_frame_real, disc_frame_wrong, disc_frame_fake):
    return (bce(tf.ones_like(disc_frame_real), disc_frame_real) + bce(tf.zeros_like(disc_frame_wrong), disc_frame_wrong) + bce(tf.zeros_like(disc_frame_fake), disc_frame_fake)) / 3.

@tf.function
def motion_loss(disc_motion_real, disc_motion_wrong, disc_motion_fake):  # only for generator
    return (bce(tf.ones_like(disc_motion_real), disc_motion_real) + bce(tf.zeros_like(disc_motion_wrong), disc_motion_wrong) + bce(tf.zeros_like(disc_motion_fake), disc_motion_fake)) / 3.

@tf.function
def discriminator_loss(video_loss, frame_loss, motion_loss):
    return (video_loss + frame_loss + motion_loss) / 3.

# reduce_mean for batch
@tf.function
def generator_loss(disc_video_fake, disc_frame_fake, disc_motion_fake):
    return (bce(tf.ones_like(disc_video_fake), disc_video_fake) + bce(tf.ones_like(disc_frame_fake), disc_frame_fake) + bce(tf.ones_like(disc_motion_fake), disc_motion_fake)) / 3.
