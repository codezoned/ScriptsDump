#Model achieves greater than 93% accuracy with CIFAR10
model = None
# https://keras.io/
!pip install -q keras
import keras

import keras
from keras.datasets import cifar10
from keras.models import Model, Sequential
from keras.layers import Dense, Dropout, Flatten, Input, AveragePooling2D, merge, Activation, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.layers import Concatenate
from keras.optimizers import Adam

# this part will prevent tensorflow to allocate all the avaliable GPU Memory
# backend
import tensorflow as tf
from keras import backend as k

# determine Loss function and Optimizer
from keras.optimizers import SGD
from keras.regularizers import l2
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, Callback
import numpy as np
import scipy
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# 1. Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Hyperparameters
batch_size = 128
num_classes = 10
epochs = 50
l = 16
num_filter = 12
compression = 0.5
growth_rate = 12
dropout_rate = 0
weight_decay=1e-4

# Don't pre-allocate memory; allocate as-needed
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

# Create a session with the above options specified.
k.tensorflow_backend.set_session(tf.Session(config=config))

def resize(X_train, height, width):
  new_shape = (width,height,3)
  X_train_new = np.empty(shape=(X_train.shape[0],)+new_shape)
  for idx in range(X_train.shape[0]):
    X_train_new[idx] = scipy.misc.imresize(X_train[idx], new_shape)
  return X_train_new

def preprocess_input(x):
    x = x[..., ::-1]
    x[..., 0] -= 103.939
    x[..., 1] -= 116.779
    x[..., 2] -= 123.68
    x *= 0.017
    return x  

def save_to_drive(epoch):  
  title = 'DenseNet-CIFAR10' + str(epoch) + '.h5'
  model_file = drive.CreateFile({'title' : title})
  model_file.SetContentFile('DenseNet-40-12-CIFAR10.h5')
  model_file.Upload()

  # download to google drive
  drive.CreateFile({'id': model_file.get('id')})  
  
def get_from_drive(idv):
  gauth = GoogleAuth()
  gauth.credentials = GoogleCredentials.get_application_default()
  drive = GoogleDrive(gauth)
  last_weight_file = drive.CreateFile({'id': idv}) 
  last_weight_file.GetContentFile('DenseNet-40-12-CIFAR10.h5')    
  
class EarlyStoppingByAccuracy(Callback):
    def __init__(self, monitor='val_acc', mode='max', value=0.92, verbose=0):
        super(Callback, self).__init__()
        self.monitor = monitor
        self.value = value
        self.verbose = verbose

    def on_epoch_end(self, epoch, logs={}):
        current = logs.get(self.monitor)
        lr = self.model.optimizer.lr
        # If you want to apply decay.
        if k.get_value(self.model.optimizer.iterations) == 100:
          k.set_value(self.model.optimizer.lr, 0.01)
          print("Updating Learning rate", 0.01)
        print("Current learning rate", k.get_value(self.model.optimizer.lr))    
        if current is None:
            warnings.warn("Early stopping requires %s available!" % self.monitor, RuntimeWarning)
        #if k.get_value(self.model.optimizer.iterations)%5 == 0:
        #save_to_drive(k.get_value(self.model.optimizer.iterations))        
        if current >= self.value:
            if self.verbose > 0:
                print("Epoch %05d: early stopping THR" % epoch)
            self.model.stop_training = True

# Load CIFAR10 Data
(x_train, y_train), (x_test, y_test) = cifar10.load_data()


x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train = preprocess_input(x_train)
x_test = preprocess_input(x_test)

x_train_24 = resize(x_train, 24, 24)
x_test_24 = resize(x_test, 24, 24)



generator = ImageDataGenerator(rotation_range=15,
                               width_shift_range=5./32,
                               height_shift_range=5./32,
                               horizontal_flip=True)
lr_reducer = ReduceLROnPlateau(monitor='val_acc', factor=0.8,
                                    cooldown=0, patience=5, min_lr=0.01)
weights_file="DenseNet-40-12-CIFAR10.h5"
model_checkpoint= ModelCheckpoint(weights_file, monitor="val_acc", save_best_only=False,
                                  save_weights_only=True, verbose=1)
early_stopping = EarlyStoppingByAccuracy(monitor='val_acc', value=0.92, verbose=1)
callbacks=[early_stopping, model_checkpoint]


# convert to one hot encoing 
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# Dense Block
def add_denseblock(input, num_filter = 12, num_input_filter=12, dropout_rate = 0.2):
    global compression
    global weight_decay
    global growth_rate
    out_filter = num_input_filter
    temp = input
    bc = True
    for _ in range(l):
        inter_channel = num_filter * 4
        
        BatchNorm = BatchNormalization(epsilon=1.1e-5)(temp)
        relu = Activation('relu')(BatchNorm)
        if bc:
          Conv2D_1_1 = Conv2D(inter_channel, (1, 1), kernel_initializer='he_normal', padding='same', use_bias=False,
                   kernel_regularizer=l2(weight_decay))(relu)              
          BatchNorm = BatchNormalization(epsilon=1.1e-5)(Conv2D_1_1)
          relu = Activation('relu')(BatchNorm)              

        Conv2D_3_3 = Conv2D(int(num_filter*compression), (3,3), kernel_initializer='he_normal', use_bias=False, padding='same')(relu)
        if dropout_rate>0:
          Conv2D_3_3 = Dropout(dropout_rate)(Conv2D_3_3)
        concat = Concatenate(axis=-1)([temp,Conv2D_3_3])
        temp = concat
        out_filter += num_filter
        
    return temp, out_filter

def add_transition(input, num_filter = 12, dropout_rate = 0.2):
    global weight_decay
    BatchNorm = BatchNormalization()(input)
    relu = Activation('relu')(BatchNorm)
    Conv2D_BottleNeck = Conv2D(int(num_filter*compression), (1,1), use_bias=False, padding='same', kernel_initializer='he_normal', kernel_regularizer=l2(weight_decay))(relu)
    if dropout_rate>0:
      Conv2D_BottleNeck = Dropout(dropout_rate)(Conv2D_BottleNeck)
    avg = AveragePooling2D(pool_size=(2,2))(Conv2D_BottleNeck)
    
    return avg, int(num_filter*compression)

def output_layer(input):
    global compression
    BatchNorm = BatchNormalization()(input)
    relu = Activation('relu')(BatchNorm)
    AvgPooling = AveragePooling2D(pool_size=(2,2))(relu)
    flat = Flatten()(AvgPooling)
    output = Dense(num_classes, activation='softmax')(flat)
    
    return output

def run_on_dataset(train_x, test_x, epochs, initial_epoch, load_weights=False, learning_rate=0.1, aug=True):  
  global model
  batch_size = 64
  if model==None:
    img_height, img_width, channel = train_x.shape[1],train_x.shape[2],train_x.shape[3]
    input = Input(shape=(img_height, img_width, channel,))
    First_Conv2D = Conv2D(num_filter*2, (3,3), use_bias=False ,padding='same', kernel_initializer='he_normal', kernel_regularizer=l2(weight_decay))(input)

    First_Block, out_filters = add_denseblock(First_Conv2D, num_filter, num_filter*2, dropout_rate)
    First_Transition, out_filters = add_transition(First_Block, out_filters, dropout_rate)
    Second_Block, out_filters = add_denseblock(First_Transition, num_filter, out_filters, dropout_rate)
    Second_Transition, out_filters = add_transition(Second_Block, out_filters, dropout_rate)
    Third_Block, out_filters = add_denseblock(Second_Transition, num_filter, out_filters, dropout_rate)
    Third_Transition, out_filters = add_transition(Third_Block, out_filters, dropout_rate)
    Last_Block, out_filters = add_denseblock(Third_Transition,  num_filter, out_filters, dropout_rate)
    output = output_layer(Last_Block)    
    model = Model(inputs=[input], outputs=[output])

    sgd = SGD(lr=learning_rate, decay=0.0001, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])
    generator.fit(train_x, augment=True)
  if(load_weights):
    model.load_weights("DenseNet-40-12-CIFAR10.h5")
  model.summary()    
  if aug==True:  
    steps_per_epoch = (len(train_x)*2)//batch_size    
    model.fit_generator(generator.flow(train_x, y_train, batch_size=batch_size),
              steps_per_epoch=steps_per_epoch,
              epochs=epochs,
              verbose=1,
              initial_epoch=initial_epoch,          
              validation_data=(test_x, y_test),
              callbacks=callbacks)      
  else:  
    model.fit(train_x, y_train, batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              initial_epoch=initial_epoch,          
              validation_data=(test_x, y_test),
              callbacks=callbacks) 