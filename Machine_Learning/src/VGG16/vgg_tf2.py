import tensorflow as tf 
from tensorflow.keras.models import Model
from tensorflow.keras.losses import MSE
from tensorflow.keras.optimizers import Adam
import numpy as np

class Vgg16(tf.keras.Model):
	def __init__(self,output_nodes):
		super(Vgg16, self).__init__()
		# layers needed
		self.conv1_1 = tf.keras.layers.Conv2D(
					input_shape=[None,28,28,1],filters=64, kernel_size=3,
					padding="same", activation="relu")
		self.conv1_2 = tf.keras.layers.Conv2D(
					filters=64, kernel_size=3,
					padding="same", activation="relu")
		self.conv2_1 = tf.keras.layers.Conv2D(
					filters=128, kernel_size=3,
					padding="same", activation="relu")
		self.conv2_2 = tf.keras.layers.Conv2D(
					filters=128, kernel_size=3,
					padding="same", activation="relu")
		self.conv3_1 = tf.keras.layers.Conv2D(
					filters=256,kernel_size=3,
					padding="same", activation="relu")
		self.conv3_2 = tf.keras.layers.Conv2D(
					filters=256,kernel_size=3,
					padding="same", activation="relu")
		self.conv3_3 = tf.keras.layers.Conv2D(
					filters=256,kernel_size=3,
					padding="same", activation="relu")
		
		self.conv4_1 = tf.keras.layers.Conv2D(
					filters=512, kernel_size=3,
					padding="same", activation="relu")
		self.conv4_2 = tf.keras.layers.Conv2D(
					filters=512, kernel_size=3,
					padding="same", activation="relu")
		self.conv4_3 = tf.keras.layers.Conv2D(
					filters=512, kernel_size=3,
					padding="same", activation="relu")
		self.conv5_1 = tf.keras.layers.Conv2D(
					filters=512, kernel_size=3,
					padding="same", activation="relu")
		self.conv5_2 = tf.keras.layers.Conv2D(
					filters=512, kernel_size=3,
					padding="same", activation="relu")
		self.conv5_3 = tf.keras.layers.Conv2D(
					filters=512, kernel_size=3,
					padding="same", activation="relu")
		self.dense1_1 = tf.keras.layers.Dense(
					units=4096, activation="relu")
		self.dense1_2 = tf.keras.layers.Dense(
					units=4096, activation="relu")
		self.dense2 = tf.keras.layers.Dense(
					units=output_nodes, activation="softmax")
		self.maxPool = tf.keras.layers.MaxPool2D(
					pool_size=2, strides=2, padding="same")
		self.flatten = tf.keras.layers.Flatten()

	def call(self,input):
		# ops 
		x = self.conv1_1(input)
		x = self.conv1_2(x)
		x = self.maxPool(x)
		x = self.conv2_1(x)
		x = self.conv2_2(x)
		x = self.maxPool(x)
		x = self.conv3_1(x)
		x = self.conv3_2(x)
		x = self.conv3_3(x)
		x = self.maxPool(x)
		x = self.conv4_1(x)
		x = self.conv4_2(x)
		x = self.conv4_3(x)
		x = self.maxPool(x)
		x = self.conv5_1(x)
		x = self.conv5_2(x)
		x = self.conv5_3(x)
		x = self.maxPool(x)
		x = self.flatten(x)
		x = self.dense1_1(x)
		x = self.dense1_2(x)
		x = self.dense2(x)
		return x


network = Vgg16(10)
# network.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train = (x_train.reshape(-1, 28, 28, 1) / 255).astype(np.float32)
# x_train, x_test = x_train / 255.0, x_test / 255.0
y_train = np.eye(10)[y_train].astype(np.float32)
x_train = x_train[:100]
y_train = y_train[:100]



input_layer = tf.keras.layers.Input(shape=(28,28,1))
output_layer = network(input_layer)
training_model = Model(inputs=input_layer,outputs=output_layer)
optim = Adam()

for i in range(100):
	with tf.GradientTape(watch_accessed_variables=False) as tape:
		tape.watch(training_model.trainable_variables)
		preds = training_model(x_train)
		loss = MSE(preds, y_train)
		cost = tf.reduce_mean(loss)
		grads = tape.gradient(loss, training_model.trainable_variables)
		optim.apply_gradients(zip(grads, training_model.trainable_variables))
	print(cost)




