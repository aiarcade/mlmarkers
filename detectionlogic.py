
import cv2
import numpy as np

import tensorflow as tf
import numpy as np

from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import img_to_array



class MLDetection(object):

    def __init__(self,line_length=100,line_width=10,is_write=True,out_dir="out",learning_width=0):
        
        self.line_length=line_length
        self.line_width=line_width
        self.is_write=is_write
        self.out_dir=out_dir
        self.model = tf.keras.models.load_model('markersmodel.h5')
        self.model.summary()
        if learning_width==0:
            learning_width=self.model.layers[0].output_shape[1]+2
        if K.image_data_format() == 'channels_first':
            self.input_shape = (1, learning_width, learning_width)
        else:
            self.input_shape = (learning_width, learning_width, 1)
        self.detectedImage=None
        
    def detectml(self,window):
        window=cv2.resize(window,(self.input_shape[0],self.input_shape[0]) , interpolation = cv2.INTER_NEAREST) 
        window = img_to_array(window)
        window=window.reshape((1, window.shape[0], window.shape[1], window.shape[2]))
        score = self.model.predict(window, verbose=0)
        if score==1:
            return True
        else:
            return False
    def crop_rect(self,gray, rect):
        # get the parameter of the small rectangle
        center, size, angle = rect[0], rect[1], rect[2]
        center, size = tuple(map(int, center)), tuple(map(int, size))

        # get row and col num in img
        height, width = gray.shape[0],gray.shape[1]

        # calculate the rotation matrix
        M = cv2.getRotationMatrix2D(center, angle, 1)
        # rotate the original image
        img_rot = cv2.warpAffine(gray, M, (width, height))

        # now rotated rectangle becomes vertical and we crop it
        img_crop = cv2.getRectSubPix(img_rot, size, center)

        return img_crop, img_rot
    def process(self,image_src):
        self.image=image_src
        processCopy=image_src.copy()
        image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))); 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _ , gray = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

        n_labals, labels, stats, centroids = cv2.connectedComponentsWithStats(gray,8)

        lines=range(1,n_labals)
        

        blank=np.zeros(gray.shape).astype(np.uint8)


        for line in lines:      
            org_gray=gray.copy()
            c =np.asarray(np.where(labels == line)).T
            top = tuple(reversed(tuple(c[np.argmin(c[:, 1])])))
            bottom= tuple(reversed(tuple(c[np.argmax(c[:, 1])])))
            rect=cv2.minAreaRect(np.array([top,bottom]))
            #print(rect)
            lrect=[list(i) for i in rect[0:2]]
            lrect[1][1]=self.line_width #width of marker
            lrect[1][0]=self.line_length #length of marker
            lrect.append(rect[2])           
            
            rect=(tuple(lrect[0]),tuple(lrect[1]),rect[2])
            
            rows,cols = gray.shape[:2]
            box = cv2.boxPoints(rect) 
            box = np.int0(box)

            present=self.detectml(self.crop_rect(gray, rect)[0])
            #print(box)
            if present:
                stencil  = np.zeros(gray.shape).astype(np.uint8)
                cv2.fillPoly(stencil,[box],255)
                sel      = stencil != 255 # select everything that is not mask_value
                org_gray[sel] = 0         # and fill it with fill_color
                cv2.imwrite(self.out_dir+"/marker"+str(line)+".jpg",org_gray)
                cv2.drawContours(processCopy,[box],0,(0,0,255),1) 
        self.detectedImage=processCopy.copy()   
        
    def getProcessedImage(self):
        return self.detectedImage



#image = cv2.imread("2.png")
#ml=MLDetection(image)
#ml.process()






# image = cv2.imread("2.png")
# # Changing the colour-space
# image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))); 
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _ , gray = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)

# n_labals, labels, stats, centroids = cv2.connectedComponentsWithStats(gray,8)

# lines=[]

# for i in range(2,n_labals):
#     a=stats[i,cv2.CC_STAT_AREA]
#     if a<250 and a> 100:
#         lines.append(i)


# for line in lines:
   
#     org_gray=gray.copy()
#     c =np.asarray(np.where(labels == line)).T
#     top = tuple(reversed(tuple(c[np.argmin(c[:, 1])])))
#     bottom= tuple(reversed(tuple(c[np.argmax(c[:, 1])])))
#     rect=cv2.minAreaRect(np.array([top,bottom]))
#     print(rect)
#     lrect=[list(i) for i in rect[0:2]]
#     lrect[1][1]=10 #width of marker
#     lrect[1][0]=100 #length of marker
#     lrect.append(rect[2])
    
    
#     rect=(tuple(lrect[0]),tuple(lrect[1]),rect[2])
    
#     rows,cols = gray.shape[:2]
#     box = cv2.boxPoints(rect) 
#     box = np.int0(box)

#     present=detectml(model,crop_rect(gray, rect)[0],input_shape)
#     if present:
#         stencil  = np.zeros(gray.shape).astype(np.uint8)
#         cv2.fillPoly(stencil,[box],255)
#         sel      = stencil != 255 # select everything that is not mask_value
#         org_gray[sel] = 0         # and fill it with fill_color

#         cv2.imwrite("out/line"+str(line)+".jpg",org_gray)
       

    


    
#     #[vx,vy,x,y] = cv2.fitLine(box, cv2.DIST_L2,0,0.01,0.01)
#     #lefty = int((-x*vy/vx) + y)
#     #righty = int(((cols-x)*vy/vx)+y)
#     #cv2.line(img,bottom,(x,y),(255,255,255),2)
#     #cv2.line(img,(cols-1,righty),(0,lefty),(255,255,255),2)
#     #cv2.drawContours(img,[box],-1,(255,255,255),-1)  
#     # 
#     #img=np.uint8(img) 
#     #cv2.imwrite("out/line"+str(line)+".jpg",crop_rect(gray, rect)[0])
#     #
   
#     #


