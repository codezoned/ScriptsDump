"""
This file describes implementation of a basic CNN made using Tensorflow and trained and tested with MNIST dataset.
Initially we have all the required dependencies imported.

create_model() describes the CNN architecture used for training a model

plot() is used to plot the images along with their predicted/true labels.

"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2

# CNN Model 
def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3,3), activation="relu", input_shape=(28,28,1)),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.Conv2D(32, (2,2), activation="relu"),
        tf.keras.layers.MaxPooling2D((2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(10, activation="softmax")
    ])
    return model

# Plot images with labels
def plot(subset_x, subset_y):
    for i in range(len(subset_y)):
    plt.figure(figsize=(10,20))
    ax = plt.subplot(len(subset_y)/2,2,i+1)
    img = subset_x[i]
    ax.imshow(img)
    plt.show()
    print("LABEL : ",subset_y[i])
    print()

# Load Mnist dataset from tensorflow datasets
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the pixel values and convert the lables to one-hot vectors
x_train = x_train/255.
x_test = x_test/255.
x_train = x_train.reshape((-1,28,28,1))
x_test = x_test.reshape((-1,28,28,1))
y_train = tf.one_hot(y_train, depth=10)
y_test = tf.one_hot(y_test, depth=10)

# Create and compile the Model
my_model = create_model()
my_model.compile(optimizer = tf.keras.optimizers.Adam(lr=0.001), loss="categorical_crossentropy", metrics=["accuracy"])

# Fit the created model and store the information for plotting of loss and accuracy curves
history = my_model.fit(x_train, y_train, validation_split=0.1, epochs=5, batch_size=32, shuffle=True, verbose=1)

# Evaluate the model using the test data
loss, acc = my_model.evaluate(x_test, y_test)

# Make Predictions
y_predictions = my_model.predict_classes(x_test)

subset_x = x_test[0:10]
subset_y = y_predictions[0:10]

# Used to plot the predicted labels along with images.
plot(subset_x, subset_y)

