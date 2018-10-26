import tensorflow as tf
import random
import os
import cv2
import numpy as np
import scipy.misc 

import matplotlib.pyplot as plt



slim = tf.contrib.slim

HEIGHT, WIDTH, CHANNEL = 64, 64, 3
BATCH_SIZE = 9
EPOCH = 5000
version = 'newAnime'
newPoke_path = './' + version


def lrelu(x, n, leak=0.2):
    return tf.maximum(x, leak * x, name=n)

def save_images(images, size, image_path):
  return imsave(inverse_transform(images), size, image_path)
  
def inverse_transform(images):
  return (images+1.)/2.

def merge(images, size):
  h, w = images.shape[1], images.shape[2]
  if (images.shape[3] in (3,4)):
    c = images.shape[3]
    img = np.zeros((h * size[0], w * size[1], c))
    for idx, image in enumerate(images):
      i = idx % size[1]
      j = idx // size[1]
      img[j * h:j * h + h, i * w:i * w + w, :] = image
    return img
  elif images.shape[3]==1:
    img = np.zeros((h * size[0], w * size[1]))
    for idx, image in enumerate(images):
      i = idx % size[1]
      j = idx // size[1]
      img[j * h:j * h + h, i * w:i * w + w] = image[:,:,0]
    return img
  else:
    raise ValueError('in merge(images,size) images parameter '
                     'must have dimensions: HxW or HxWx3 or HxWx4')

def imsave(images, size, path):
  image = np.squeeze(merge(images, size))
  return scipy.misc.imsave(path, image)    
    
    
    
def process_data():
	cur_dir = os.getcwd()
	file_dir = os.path.join(cur_dir,'data/image')
	images=[]
	for pic in os.listdir(file_dir):
		images.append(os.path.join(file_dir,pic))
	dataset = tf.convert_to_tensor(images,dtype=tf.string)
	images_queue = tf.train.slice_input_producer([dataset])
	data = tf.read_file(images_queue[0])
	image = tf.image.decode_jpeg(data,channels=CHANNEL)
	image = tf.image.random_flip_left_right(image)
	image = tf.image.random_brightness(image, max_delta=0.1)
	image = tf.image.random_contrast(image, lower=0.9, upper=1.1)
	size = [HEIGHT,WIDTH]
	image = tf.image.resize_images(image, size)
	image.set_shape([HEIGHT, WIDTH, CHANNEL])
	image = tf.cast(image, tf.float32)
	image = image / 255.0

	images_batch = tf.train.shuffle_batch(
	    [image], batch_size=BATCH_SIZE,
	    num_threads=4, capacity=200 + 3 * BATCH_SIZE,
	    min_after_dequeue=200)
	num_images = len(images)

	return images_batch, num_images
	

def generator(input,input_dim,is_train,reuse=False):
	c1 ,c2, c3, c4, c5 = 512, 256, 128, 64, 32  # numero de canal
	s4 = 1
	output_dim = CHANNEL  # RGB image
	with tf.variable_scope('gen') as scope:
		if reuse:
			scope.reuse_variables()
		w1 = tf.get_variable('weights1', shape=[input_dim, 4 * 4 * c1], dtype=tf.float32,
		                     initializer=tf.truncated_normal_initializer(stddev=0.02))
		b1 = tf.get_variable('biases1',shape = [4*4*c1],dtype=tf.float32,
		                     initializer=tf.constant_initializer(0.0))
		fc1 = tf.matmul(input,w1)+b1

		conv_0 = tf.reshape(fc1, shape=[-1, 4, 4, c1], name='conv0')
		batch_norm_0 = bn1 = tf.contrib.layers.batch_norm(conv_0, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn0')
		act_conv_0 = lrelu(batch_norm_0,"activation_conv_0")
		conv_1 = tf.layers.conv2d_transpose(act_conv_0, c2, kernel_size=[5, 5], strides=[2, 2], padding="SAME",
                                           kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
                                           name='conv1')
		batch_norm_1 = tf.contrib.layers.batch_norm(conv_1, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn1')
		act_conv_1 = lrelu(batch_norm_1,"activation_conv_1")
		conv_2 = tf.layers.conv2d_transpose(act_conv_1,c3,kernel_size=[5,5],strides=[2,2],padding='SAME',
											kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
											name='conv2')
		batch_norm_2 = tf.contrib.layers.batch_norm(conv_2, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn2')
		act_conv_2 = lrelu(batch_norm_2,"activation_conv_2")
		conv_3 = tf.layers.conv2d_transpose(act_conv_2,c4,kernel_size=[5,5],strides=[2,2],padding='SAME',
											kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
											name='conv3')
		batch_norm_3 = tf.contrib.layers.batch_norm(conv_3, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn3')
		act_conv_3 = lrelu(batch_norm_3,"activation_conv_3")
		
		conv_output = tf.layers.conv2d_transpose(act_conv_3,output_dim,kernel_size=[5,5],strides=[2,2],padding='SAME',
											kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
											name='conv_ouput')
		output_act = lrelu(conv_output,"final_output")
		return output_act


def discriminator(input,is_train,reuse=False):
	c1,c2,c3,c4 = 64, 128, 256, 512 
	
	with tf.variable_scope("discriminator") as scope:
		if reuse:
			scope.reuse_variables()
		conv_1 = tf.layers.conv2d(input, c1, kernel_size=[5, 5], strides=[2, 2], padding="SAME",
		                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
		                         name='conv1')
		batch_norm_1 = tf.contrib.layers.batch_norm(conv_1, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn1')
		act_conv_1 = lrelu(batch_norm_1, n='activation_conv_1')
		conv_2 = tf.layers.conv2d(act_conv_1, c2, kernel_size=[5, 5], strides=[2, 2], padding="SAME",
		                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
		                         name='conv2')
		batch_norm_2 = tf.contrib.layers.batch_norm(conv_2, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn2')
		act_conv_2 = lrelu(batch_norm_2, n='activation_conv_2')
		conv_3 = tf.layers.conv2d(act_conv_2, c3, kernel_size=[5, 5], strides=[2, 2], padding="SAME",
		                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
		                         name='conv3')
		batch_norm_3 = tf.contrib.layers.batch_norm(conv_3, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn3')
		act_conv_3 = lrelu(batch_norm_3, n='activation_conv_3')

		conv_4 = tf.layers.conv2d(act_conv_3, c4, kernel_size=[5, 5], strides=[2, 2], padding="SAME",
		                         kernel_initializer=tf.truncated_normal_initializer(stddev=0.02),
		                         name='conv4')
		batch_norm_4 = tf.contrib.layers.batch_norm(conv_4, is_training=is_train, epsilon=1e-5, decay=0.9,
		                                   updates_collections=None, scope='bn4')
		act_conv_4 = lrelu(batch_norm_4, n='activation_conv_4')

		dim = int(np.prod(act_conv_4.get_shape()[4:]))

		input_fc = tf.reshape(act_conv_4,shape=[-1,dim],name="input_fc")

		w1 = tf.get_variable('weights2', shape=[input_fc.shape[-1],1], dtype=tf.float32,
		                     initializer=tf.truncated_normal_initializer(stddev=0.02))
		b1 = tf.get_variable('biases2',shape = [1],dtype=tf.float32,
		                     initializer=tf.constant_initializer(0.0))
		fc1 = tf.matmul(input_fc,w1)+b1

		output = tf.nn.sigmoid(fc1)

		return fc1


def train():
	input_dim = 100
	real_image = tf.placeholder(tf.float32, shape=[None, HEIGHT, WIDTH, CHANNEL], name='real_image')
	input_fake = tf.placeholder(tf.float32, shape=[None, input_dim], name='noise_image')
	is_train = tf.placeholder(tf.bool, name='is_train')
	
	
	fake_image = generator(input_fake,input_dim,is_train)
	
	real_result = discriminator(real_image, is_train)
	fake_result = discriminator(fake_image, is_train, reuse=True)
	
	d_loss = tf.reduce_mean(fake_result)-tf.reduce_mean(real_result)	
	g_loss = -tf.reduce_mean(fake_result)
	
	t_vars = tf.trainable_variables()
	d_vars = [var for var in t_vars if 'dis' in var.name]
	g_vars = [var for var in t_vars if 'gen' in var.name]
	trainer_d = tf.train.RMSPropOptimizer(learning_rate=2e-4).minimize(d_loss, var_list=d_vars)
	trainer_g = tf.train.RMSPropOptimizer(learning_rate=2e-4).minimize(g_loss, var_list=g_vars)
	
	d_clip = [v.assign(tf.clip_by_value(v, -0.01, 0.01)) for v in d_vars]
	
	batch_size = BATCH_SIZE
	image_batch, samples_num = process_data()
	
	batch_num = int(samples_num / batch_size)
	total_batch = 0
	sess = tf.Session()
	saver = tf.train.Saver()
	sess.run(tf.global_variables_initializer())
	sess.run(tf.local_variables_initializer())
	save_path = saver.save(sess, "tmp/model2.ckpt")
	ckpt = tf.train.latest_checkpoint(version)
	saver.restore(sess, save_path)
	coord = tf.train.Coordinator()
	threads = tf.train.start_queue_runners(sess=sess, coord=coord)
	
	print('total training sample num:%d' % samples_num)
	print('batch size: %d, batch num per epoch: %d, epoch num: %d' % (batch_size, batch_num, EPOCH))
	print('start training...')
	dLossArray = []
	iArray = []
	gLossArray = []
	
	for i in range(0,EPOCH):
		print(i)
		for j in range(batch_num):
			print(j)
			disc_iterations=5
			gen_iterations=1
			train_noise = np.random.uniform(-1.0, 1.0, size=[batch_size, input_dim]).astype(np.float32)
			train_noise = np.random.uniform(-1.0, 1.0, size=[batch_size, input_dim]).astype(np.float32)
			for k in range(disc_iterations):
				print(k)
				train_image = sess.run(image_batch)
				# wgan clip weights
				sess.run(d_clip)
				# Update the discriminator
				_, dLoss = sess.run([trainer_d, d_loss],
				                feed_dict={input_fake: train_noise, real_image: train_image, is_train: True})
			for k in range(gen_iterations):
				_, gLoss = sess.run([trainer_g, g_loss],
                                    feed_dict={input_fake: train_noise, is_train: True})
		    
		if i % 30 == 0:
			if not os.path.exists('model/' + version):
				os.makedirs('model/' + version)
			saver.save(sess, 'model/' + version + '/' + str(i))
		if i % 10 == 0:
           	# save images
			if not os.path.exists(newPoke_path):
				os.makedirs(newPoke_path)
			sample_noise = np.random.uniform(-1.0, 1.0, size=[batch_size, input_dim]).astype(np.float32)
			imgtest = sess.run(fake_image, feed_dict={input_fake: sample_noise, is_train: False})
		# imgtest = imgtest * 255.0
		# imgtest.astype(np.uint8)
			save_images(imgtest, [3, 3], 'data/imageval/' + str(i) + '.png')
			print('train:[%d],d_loss:%f,g_loss:%f' % (i, dLoss, gLoss))
			dLossArray.append(dLoss)
			gLossArray.append(gLoss)
			iArray.append(i)  
			print(dLossArray, gLossArray, iArray)				
			plt.plot(dLossArray,'r-', gLossArray,'g-')
			plt.ylabel('loss')
			plt.xlabel('x10 epochs')
			plt.savefig('plot'+ str(i)+'.png')
	coord.request_stop()
	coord.join(threads)


if __name__=='__main__':
	train()
