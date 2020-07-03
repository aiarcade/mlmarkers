from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten,Activation ,Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
#from cnnmodel import *
from tensorflow.keras import backend as K
from tensorflow.keras.layers.experimental import RandomFourierFeatures

class Model():
    def __init__(self,modetype)

        
        if modeltype==0: 
            self.model = Sequential()
            
            self.model.add(Conv2D(32, (3, 3), input_shape=input_shape))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

            self.model.add(Conv2D(32, (3, 3)))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

            self.model.add(Conv2D(64, (3, 3)))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
            self.model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
            self.model.add(Dense(64))
            self.model.add(Activation('relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(1))
            self.model.add(Activation('sigmoid'))        
        if modeltype==1:
            model = Sequential()
            
            self.model.add(Conv2D(32, (3, 3), input_shape=input_shape))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

            self.model.add(Conv2D(32, (3, 3)))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
            self.model.add(Conv2D(64, (3, 3)))
            self.model.add(Activation('relu'))
            self.model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
            self.model.add(Flatten())
            self.model.add(RandomFourierFeatures(output_dim=4096, scale=10.0, kernel_initializer="gaussian"))
            self.model.add(Dense(64))
            self.model.add(Activation('relu'))
            self.model.add(Dropout(0.5))
            self.model.add(Dense(1))
            self.model.add(Activation('sigmoid')) 
    def getTfModel(self):
        return self.model