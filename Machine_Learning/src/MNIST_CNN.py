# CNN achieves >99.3% accuracy within 20 epochs 

from keras.datasets import mnist
import keras
import warnings
num_classes = 10
(x_train, y_train), (x_test, y_test) = mnist.load_data()
img_height, img_width = x_train.shape[1],x_train.shape[2]

# convert to one hot encoing 
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
from keras.preprocessing.image import ImageDataGenerator
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train/= 255
x_test/= 255
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
from keras.layers import Convolution2D, MaxPooling2D, Conv2D
from keras.callbacks import Callback, ModelCheckpoint

model = Sequential()
model.add(Conv2D(32, 3, input_shape=(28,28,1)))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Conv2D(32, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Conv2D(10, 1))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(10, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Conv2D(10, 3))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(Flatten())
model.add(Dense(10))
model.add(BatchNormalization())
model.add(Activation("softmax"))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()


class EarlyStoppingByAccuracy(Callback):
    def __init__(self, monitor='val_acc', mode='max', value=0.98, verbose=0):
        super(Callback, self).__init__()
        self.monitor = monitor
        self.value = value
        self.verbose = verbose

    def on_epoch_end(self, epoch, logs={}):
        current = logs.get(self.monitor)
        if current is None:
            warnings.warn("Early stopping requires %s available!" % self.monitor, RuntimeWarning)
        
        if current >= self.value:
            if self.verbose > 0:
                print("Epoch %05d: early stopping THR" % epoch)
            self.model.stop_training = True

callbacks = [
    EarlyStoppingByAccuracy(monitor='val_acc', value=0.992, verbose=1),
    ModelCheckpoint(filepath='/tmp/weights.hdf5', monitor='val_loss', save_best_only=True, verbose=0),
]          

model.fit(x_train, y_train,
                    batch_size=256,
                    epochs=30,
                    verbose=1,
                    validation_data=(x_test, y_test),
                    callbacks=callbacks)