import numpy as np
import pandas as pd
import  cv2
import cv2 as cv
from scipy import ndimage
import math

from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten,Activation ,Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
#from cnnmodel import *
from tensorflow.keras import backend as K

class GenDataSet(QRunnable):
    def __init__(self,no_samples,output_dir,output_size,pgbar,button):
        super(GenDataSet, self).__init__()
        self.no_samples=no_samples
        self.output_dir=output_dir
        self.train_progess=0
        self.dia_len=0
        self.pgbar=pgbar
        self.trbutton=button
    def setImages(self,input_images):
        self.image_list=input_images
        largest_width=0
        largest_height=0
        for image in self.image_list:
            if image.shape[1]>largest_width:
                largest_width=image.shape[1]
            if image.shape[0]>largest_height:
                largest_height=image.shape[0]
        self.output_size=(largest_width,largest_height)

    @pyqtSlot()
    def run(self):
        self.trbutton.setEnabled(False)
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        im_i=0
        self.dia_len=int(math.sqrt(self.output_size[0]**2+self.output_size[1]**2))
        
        output_size=[self.dia_len,self.dia_len]
        self.X=[]
        self.y=[]
        for image in self.image_list:
             gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
             cv2.imwrite("train/positive/"+str(im_i)+".jpg",gray)
             cim=self.crop(gray,[50,50],True)
             cv2.imwrite("train/negative/"+str(im_i)+".jpg",cim)
             im_i=im_i+1
        #     alter=True
        #     for angle in range(0,90):
        #         #positive image
        #         blank=np.zeros(shape=output_size, dtype=np.uint8)
        #         rtim= ndimage.rotate(gray, angle)
        #         self.write_image(self.output_dir+"/"+str(im_i)+"_patch_p"+str(angle)+".jpg",self.combine(rtim,blank))
        #         self.y.append(1)
        #         #negative image
        #         blank=np.zeros(shape=output_size, dtype=np.uint8)
        #         cim=self.crop(rtim,[angle,angle],alter)
        #         self.write_image(self.output_dir+"/"+str(im_i)+"_patch_na"+str(angle)+".jpg",self.combine(cim,blank))
        #         self.y.append(0)
        #         alter= not alter
        #         im_i=im_i+1
        self.pgbar.setProperty("value",50)
        self.train()
        self.pgbar.setProperty("value",100)
        QtWidgets.QApplication.restoreOverrideCursor()
        self.trbutton.setEnabled(True)
        
    def write_image(self,name,image):
        #image=cv2.resize(image,self.output_size , interpolation = cv2.INTER_NEAREST) 
        #cv2.imwrite(name,image)
        self.X.append(image)


    def  crop(self,image,size,alter):
        w=size[0]
        h=size[1]
        imw=image.shape[1]
        imh=image.shape[0]
        stx=int(imw/2)
        sty=int(imh/2)
        if w>=imw:
            w=imw
        if h>=imh:
            h=imh
        #print(w,h,imw,imh,stx,sty)
        
        if w<20:
           return image[0:20, 0:20] 

        if alter==True:
            return image[sty:sty+h, stx:stx+w]
        else:
            return image[0:h,0:w]

        

        


    def rotate_image(self,image, angle):
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result

    def combine(self,overlay ,src, pos=(0,0),scale = 1):
        """
        :param src: Input Color Background Image
        :param overlay: transparent Image (BGRA)
        :param pos:  position where the image to be blit.
        :param scale : scale factor of transparent image.
        :return: Resultant Image
        """
        overlay = cv2.resize(overlay,(0,0),fx=scale,fy=scale)
        h,w= overlay.shape  # Size of pngImg
        rows,cols= src.shape  # Size of background Image
        y,x = pos[0],pos[1]    # Position of PngImage
        
        #loop over all pixels and apply the blending equation
        for i in range(h):
            for j in range(w):
                if x+i >= rows or y+j >= cols:
                    continue
                alpha = float(overlay[i][j]/255.0) # read the alpha channel 
                src[x+i][y+j] = alpha*overlay[i][j]+(1-alpha)*src[x+i][y+j]
        return src

    def train(self):
        img_width, img_height = self.dia_len,self.dia_len

        epochs = 50
        batch_size = 16

        if K.image_data_format() == 'channels_first':
            input_shape = (1, img_width, img_height)
        else:
            input_shape = (img_width, img_height, 1)
        
        batch_size=16
        
        
        train_datagen = ImageDataGenerator(
            rotation_range=40,
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            )
        train_generator = train_datagen.flow_from_directory(
            './train',  # this is the target directory
            target_size=(self.dia_len,self.dia_len),  # all images will be resized to 150x150
            batch_size=batch_size,
            class_mode='binary',
            color_mode="grayscale")  # since we use binary_crossentropy loss, we need binary labels

        # Scale images to the [0, 1] range
        


       
        model = Sequential()
        
        model.add(Conv2D(32, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))        
        print(model.summary())
# Train the model.
        model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
        model.fit_generator(
            train_generator,
            steps_per_epoch=500,
            epochs=10,
        )
        
        model.save("markersmodel.h5")  

    def progressNotice(self):
        self.train_progess=self.train_progess+1
        print(self.train_progess)
    
    def trainorg(self):
        

        num_classes = 2
        self.X=np.array(self.X)
        input_shape = (self.X.shape[1], self.X.shape[1], 1)



        # Scale images to the [0, 1] range
        x_train =self.X.astype("float32") / 255

        x_train = np.expand_dims(x_train, -1)

        print("x_train shape:", x_train.shape)

        y_train = np.array(self.y)#keras.utils.to_categorical(self.y, 1)
        # model = keras.Sequential(
        #     [
        #     keras.Input(shape=input_shape),
        #     layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        #     layers.MaxPooling2D(pool_size=(2, 2)),
        #     layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        #     layers.MaxPooling2D(pool_size=(2, 2)),
        #     layers.LSTM(32),
        #     layers.Flatten(),
        #     layers.Dense(units = 64, activation = 'relu'),
        #     layers.Dense(1, activation='sigmoid'),
        #     ]
        # )
        # model.compile(
        #     'adam',
        #     loss='binary_crossentropy',
        #     metrics=['accuracy'],
        # )
        #model=get_Model(True,x_train.shape)
        model = Sequential()
        model.add(keras.Input(shape=input_shape))
        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(64))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))        
        print(model.summary())
# Train the model.
        model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
        model.fit(
            x_train,
            y_train,
            epochs=30,
            validation_split=0.1,
           
           
        ) 
        score = model.evaluate(x_train, y_train, verbose=0)
        print("Test loss:", score[0])
        print("Test accuracy:", score[1])  
        model.save("markersmodel.h5")         



    