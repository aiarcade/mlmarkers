# import the necessary packages
import cv2
import numpy as np
import math
import argparse
import time
import cv2

import tensorflow as tf
import numpy as np
from sklearn.feature_extraction import image
from tensorflow.keras import backend as K

input_s=75
if K.image_data_format() == 'channels_first':
            input_shape = (1, input_s, input_s)
else:
    input_shape = (input_s, input_s, 1)
print(input_shape)

def collinear(p0, p1, p2):

    x1, y1, x2, y2, x3, y3 = p0[0], p0[1], p1[0], p1[1], p2[0], p2[1]
    v = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    #print(v)
    if abs(v)<50:
        return True
    else:
        return False

def labeled_components(img):
	img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]  # ensure binary
	#num_labels,labels = cv2.connectedComponents(img)
	num_labels,labels, stats, c = cv2.connectedComponentsWithStats(img,8)
	# if num_labels:
	# 	img[labels==0]=0
	# 	for i in range(1,num_labels):
	# 		img[labels==i]=255
	
	# 	return img
	# else :
	# 	return None
	line=[]
	dots=[]
	for i in range(1,num_labels):
		a=stats[i,cv2.CC_STAT_AREA]
		if a<250 and a>100:
			line.append(i)	
		if a<50 and a >10:
			dots.append(i)
	if len(line)==1 and len(dots)==2 :

		if num_labels<4 or num_labels >4:
			return False
		p1=(int(c[1][0]),int(c[1][1]))
		p2=(int(c[2][0]),int(c[2][1]))
		p3=(int(c[3][0]),int(c[3][1]))
		n=collinear(p1,p2,p3)
		
		if n:
			return True
		else:
			return False
	else:
		return False


def compute_backbone_shapes( image_shape):

    
    return np.array(
        [[int(math.ceil(image_shape[0] / stride)),
            int(math.ceil(image_shape[1] / stride))]
            for stride in [4, 8, 16, 32, 64]])

def generate_pyramid_anchors(scales, ratios, feature_shapes, feature_strides,
                             anchor_stride):
    """Generate anchors at different levels of a feature pyramid. Each scale
    is associated with a level of the pyramid, but each ratio is used in
    all levels of the pyramid.
    Returns:
    anchors: [N, (y1, x1, y2, x2)]. All generated anchors in one array. Sorted
        with the same order of the given scales. So, anchors of scale[0] come
        first, then anchors of scale[1], and so on.
    """
    # Anchors
    # [anchor_count, (y1, x1, y2, x2)]
    anchors = []
    for i in range(len(scales)):
        anchors.append(generate_anchors(scales[i], ratios, feature_shapes[i],
                                        feature_strides[i], anchor_stride))
    return np.concatenate(anchors, axis=0)


def generate_anchors(scales, ratios, shape, feature_stride, anchor_stride):
    """
    scales: 1D array of anchor sizes in pixels. Example: [32, 64, 128]
    ratios: 1D array of anchor ratios of width/height. Example: [0.5, 1, 2]
    shape: [height, width] spatial shape of the feature map over which
            to generate anchors.
    feature_stride: Stride of the feature map relative to the image in pixels.
    anchor_stride: Stride of anchors on the feature map. For example, if the
        value is 2 then generate anchors for every other feature map pixel.
    """
    # Get all combinations of scales and ratios
    scales, ratios = np.meshgrid(np.array(scales), np.array(ratios))
    scales = scales.flatten()
    ratios = ratios.flatten()

    # Enumerate heights and widths from scales and ratios
    heights = scales / np.sqrt(ratios)
    widths = scales * np.sqrt(ratios)

    # Enumerate shifts in feature space
    shifts_y = np.arange(0, shape[0], anchor_stride) * feature_stride
    shifts_x = np.arange(0, shape[1], anchor_stride) * feature_stride
    shifts_x, shifts_y = np.meshgrid(shifts_x, shifts_y)

    # Enumerate combinations of shifts, widths, and heights
    box_widths, box_centers_x = np.meshgrid(widths, shifts_x)
    box_heights, box_centers_y = np.meshgrid(heights, shifts_y)

    # Reshape to get a list of (y, x) and a list of (h, w)
    box_centers = np.stack(
        [box_centers_y, box_centers_x], axis=2).reshape([-1, 2])
    box_sizes = np.stack([box_heights, box_widths], axis=2).reshape([-1, 2])

    # Convert to corner coordinates (y1, x1, y2, x2)
    boxes = np.concatenate([box_centers - 0.5 * box_sizes,
                            box_centers + 0.5 * box_sizes], axis=1)
    return boxes
image = cv2.imread("2.png")
backbone_shapes = compute_backbone_shapes(image.shape)
print(backbone_shapes)
anchors=generate_pyramid_anchors((35,45,55),
                                             [0.5, 1, 2,3],
                                             backbone_shapes,
                                             [4, 8, 16, 32, 64],
                                             2)

model = tf.keras.models.load_model('markersmodel.h5')
model.summary()

image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imgorg=image.copy()
blank=np.zeros(shape=image.shape, dtype=np.uint8)
i=0
from keras.preprocessing.image import img_to_array
it=0
for b in anchors:
	#print(b,b[0])
	clone = blank.copy()
	org=image.copy()
	#cv2.rectangle(org, (int(b[1]), int(b[0])), (int(b[3]), int(b[2])), (255, 255, 0), 2)
	#cv2.imshow("x",org)
	#cv2.waitKey(1)
	

	
	#print((int(b[1]), int(b[0])), (int(b[3]), int(b[2])))
	window=imgorg[ int(b[0]):int(b[2]),int(b[1]):int(b[3])]
	if labeled_components(window)==False:
		continue
	if window.shape[0]==0 or window.shape[1]==0:
		continue
	#print(window.shape)
	print(it)
	it=it+1
	
	window1=window.copy()
	
	window=cv2.resize(window,(input_s,input_s) , interpolation = cv2.INTER_NEAREST) 

	
	# convert the image pixels to a numpy array
	window = img_to_array(window)
	window=window.reshape((1, window.shape[0], window.shape[1], window.shape[2]))
	

	#blank[int(b[0]):int(b[2]),int(b[1]):int(b[3])]=window1
	#cv2.imshow("Window", clone)
	#print(x.shape)
	score = model.predict(window, verbose=0)
	#print(score)
	if True:
		clone[int(b[0]):int(b[2]),int(b[1]):int(b[3])]=window1
			#cv2.rectangle(blank, (int(b[1]), int(b[0])), (int(b[3]), int(b[2])), (255, 255, 0), 2)
			#cv2.imshow("Window", blank)
		cv2.imwrite("out/bl"+str(i)+".jpg",clone)
		i=i+1
	# 	#imwrite
	# #else:
	# #	cv2.rectangle(clone, (int(b[1]), int(b[0])), (int(b[3]), int(b[2])), (255, 255, 0), 2)
	# #	cv2.imshow("Window", clone)
	




