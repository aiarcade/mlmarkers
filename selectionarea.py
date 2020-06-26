import random, sys
from PyQt5.QtCore import QPoint, QRect, QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np

class SelectionArea(QGraphicsScene):

    def __init__(self, parent = None):
    
        QGraphicsScene.__init__(self, parent)
        self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle)
        palette = QPalette()
        palette.setBrush(QPalette.Highlight, QBrush(QtCore.Qt.cyan))
        self.currentQRubberBand.setPalette(palette)
        self.currentQRubberBand.setWindowOpacity(.6)
        self.origin = QPoint()
        self.lastRect=QRect(0,0,0,0)
        self.rectItems={}
        self.itemKey=1
        self.removeLast=True
        self.rect_item=None

    def setImage(self,pixmap):
        self.pixmap=pixmap
        self.addPixmap(self.pixmap)
        self.setSceneRect(0, 0, self.pixmap.width(), self.pixmap.height())

    def setHighLightAreaLabel(self,label):
        self.highLightLabel=label
    def updateLastMarker(self):
        if self.rect_item :
            last_x=QStandardItem(str(self.lastRect.x()))
            last_y=QStandardItem(str(self.lastRect.y()))
            last_w=QStandardItem(str(self.lastRect.width()))
            last_h=QStandardItem(str(self.lastRect.height()))
            self.rectItems[self.itemKey]=self.rect_item
            self.itemKey=self.itemKey+1
            self.removeLast=False
            self.rect_item=None
            return [QStandardItem(str(self.itemKey-1)),last_x,last_y,last_w,last_h ]
        else:
            return False


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            try:  
                if self.removeLast:
                    self.removeItem(self.rect_item)
                else:    
                    self.removeLast=True
                
            except:
                self.itemKey=self.itemKey
            self.originQPoint = event.screenPos()
            self.originCropPoint = event.scenePos()

    def mouseMoveEvent(self, event):        
        self.lastRect=QtCore.QRect(self.originCropPoint.toPoint(), event.scenePos().toPoint())
        self.drawRect=QtCore.QRect(self.originQPoint, event.screenPos())
        self.currentQRubberBand.setGeometry(self.drawRect)
        subpix=self.pixmap.copy(self.lastRect)
        subpix=subpix.scaled(251, 201, QtCore.Qt.KeepAspectRatio)
        self.highLightLabel.setPixmap(subpix)
        self.currentQRubberBand.show()
        

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.currentQRubberBand.hide()
            currentQRect = self.currentQRubberBand.geometry()
            self.currentQRect = QtCore.QRect(self.originCropPoint.toPoint(), event.scenePos().toPoint())
            pen = QPen(Qt.darkRed)
            self.rect_item = QGraphicsRectItem(QRectF(self.currentQRect))
            self.rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
            self.rect_item.setPen(pen)
            self.addItem(self.rect_item) 
    def enableSelectedMarker(self,key):
        selected_rect=self.rectItems[int(key)]
        self.removeItem(selected_rect)
        self.rectItems[int(key)]=selected_rect
        pen = QPen(Qt.white)
        selected_rect.setPen(pen)
        self.addItem(selected_rect)
    def disableSelectedMarker(self,key):
        selected_rect=self.rectItems[int(key)]
        self.removeItem(selected_rect)
        self.rectItems[int(key)]=selected_rect
        pen = QPen(Qt.darkRed)
        selected_rect.setPen(pen)
        self.addItem(selected_rect)

    def convertToNPArray(self,marker_pix):
        channels_count = 4
        image = marker_pix.toImage()
        s = image.bits().asstring(self._width * self._height * channels_count)
        arr = np.fromstring(s, dtype=np.uint8).reshape((self._height, self._width, channels_count)) 
        return arr
    
    def getSetlectedMartkers(self):



    def removeSelectedMarker(self,key):
        selected_rect=self.rectItems.pop(int(key))
        self.removeItem(selected_rect)




    





