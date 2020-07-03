

from PyQt5 import QtCore, QtGui, QtWidgets
from selectionarea import SelectionArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2

import sys
from multiprocessing import Process
from generatedataset import GenDataSet
from detectionlogic import *
import os.path
import os


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(919, 715)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.trainingTab_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.trainingTab_2.setGeometry(QtCore.QRect(20, 30, 881, 641))
        self.trainingTab_2.setObjectName("trainingTab_2")
        self.trainingTab =  QtWidgets.QWidget()
        self.trainingTab.setObjectName("trainingTab")
        
        
        self.trainImageLabel = QtWidgets.QGraphicsView(self.trainingTab)
        self.trainImageLabel.setGeometry(QtCore.QRect(20, 48, 520, 540))
        self.imageScene=SelectionArea(self.trainImageLabel)
        self.trainImageLabel.setScene(self.imageScene)  

        
        
        #self.trainImageLabel.setText("")
        self.imageScene.setImage(QtGui.QPixmap("2.png"))
        self.trainImageLabel.setObjectName("trainImageLabel")
        self.groupBox = QtWidgets.QGroupBox(self.trainingTab)
        self.groupBox.setGeometry(QtCore.QRect(550, 50, 311, 501))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(207, 211, 211))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox.setPalette(palette)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.InputlineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.InputlineEdit.setGeometry(QtCore.QRect(10, 30, 181, 20))
        self.InputlineEdit.setObjectName("InputlineEdit")
        self.InputlineEdit.setText("2.png")
        self.inputSelectButton = QtWidgets.QPushButton(self.groupBox)
        self.inputSelectButton.setGeometry(QtCore.QRect(200, 20, 91, 41))
        self.inputSelectButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 291, 421))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.selectionAreaLabel = QtWidgets.QLabel(self.groupBox_2)
        self.selectionAreaLabel.setGeometry(QtCore.QRect(10, 40, 251, 201))
        self.selectionAreaLabel.setAutoFillBackground(True)
        self.selectionAreaLabel.setText("")
        self.selectionAreaLabel.setObjectName("selectionAreaLabel")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.label_4.setObjectName("label_4")
        self.markerDelButton = QtWidgets.QPushButton(self.groupBox_2)
        self.markerDelButton.setGeometry(QtCore.QRect(160, 380, 101, 41))
        self.markerDelButton.setObjectName("markerDelButton")
        self.markerAddButton = QtWidgets.QPushButton(self.groupBox_2)
        self.markerAddButton.setGeometry(QtCore.QRect(10, 380, 101, 41))
        self.markerAddButton.setObjectName("markerAddButton")
        self.markerTable = QtWidgets.QTableView(self.groupBox_2)
        self.markerTable.setGeometry(QtCore.QRect(10, 250, 251, 121))
        self.markerTable.setObjectName("markerTable")
        
        self.trainButton = QtWidgets.QPushButton(self.trainingTab)
        self.trainButton.setGeometry(QtCore.QRect(750, 570, 113, 40))
        self.trainButton.setObjectName("trainButton")
        
        self.trainingTab_2.addTab(self.trainingTab, "")
        self.detectionTab = QtWidgets.QWidget()
        self.detectionTab.setObjectName("detectionTab")
        self.trainingTab_2.addTab(self.detectionTab, "")
        self.setCentralWidget(self.centralwidget)
        

        
        self.trainingTab_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.markerTmodel = QStandardItemModel()
        self.markerTmodel.setHorizontalHeaderLabels(['Key','x','y','width','height'])
        
        self.markerTable.setModel(self.markerTmodel)
        self.markerTable.horizontalHeader().setStretchLastSection(True)
        self.markerTable.verticalHeader().hide()
        self.markerTable.setSelectionMode( QAbstractItemView.SingleSelection )
        self.markerTable.setSelectionBehavior(QTableView.SelectRows)
        self.markerTable.setColumnHidden(0,True)
        self.imageScene.setHighLightAreaLabel(self.selectionAreaLabel)
        self.markerAddButton.clicked.connect(self.addMarker)
        self.markerTable.clicked.connect(self.tableClicked)
        self.markerDelButton.clicked.connect(self.removeMarker)
        self.trainButton.clicked.connect(self.startTraining)
        self.inputSelectButton.clicked.connect(self.openInputFile)

        self.progressBar=None
        #self.progressBar = QtWidgets.QProgressBar(self.trainingTab)
        #self.progressBar.setGeometry(QtCore.QRect(550, 570, 111, 30))
        #self.progressBar.setProperty("value",0)
        #self.progressBar.setObjectName("progressBar")
        self.algComboBox = QtWidgets.QComboBox(self.trainingTab)
        self.algComboBox.setGeometry(QtCore.QRect(615, 10, 250, 26))
        self.algComboBox.setObjectName("algComboBox")
        self.algComboBox.addItem("CNN")
        self.algComboBox.addItem("SVM")
        self.algLabel = QtWidgets.QLabel(self.trainingTab)
        self.algLabel.setGeometry(QtCore.QRect(550, 10, 91, 21))
        self.algLabel.setObjectName("algLabel")
        self.algComboBox.currentTextChanged.connect(self.changeAlgorithm)

        
        self.outputEdit = QtWidgets.QLineEdit(self.detectionTab)
        self.outputEdit.setGeometry(QtCore.QRect(640, 200, 211, 21))
        self.outputEdit.setObjectName("outputEdit")
        self.outputEdit.setText("out")
        self.label = QtWidgets.QLabel(self.detectionTab)
        self.label.setGeometry(QtCore.QRect(640, 170, 101, 20))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.detectionTab)
        self.label_4.setGeometry(QtCore.QRect(640, 50, 121, 21))
        self.label_4.setObjectName("label_4")
        self.srcImageEdit = QtWidgets.QLineEdit(self.detectionTab)
        self.srcImageEdit.setGeometry(QtCore.QRect(640, 80, 121, 21))
        self.srcImageEdit.setObjectName("srcImageEdit")
        self.srcSelectButton = QtWidgets.QPushButton(self.detectionTab)
        self.srcSelectButton.setGeometry(QtCore.QRect(770, 70, 91, 40))
        self.srcSelectButton.setObjectName("srcSelectButton")
        self.detectPushButton = QtWidgets.QPushButton(self.detectionTab)
        self.detectPushButton.setGeometry(QtCore.QRect(720, 560, 140, 32))
        self.detectPushButton.setObjectName("detectPushButton")
        self.detectPushButton.clicked.connect(self.detect)
        self.srcSelectButton.clicked.connect(self.openDetectFile)
        self.srcImageEdit.setText("2.png")
        self.epochEdit = QtWidgets.QLineEdit(self.trainingTab)
        self.epochEdit.setGeometry(QtCore.QRect(680, 580, 61, 21))
        self.epochEdit.setObjectName("epochEdit")
        self.EPlabel = QtWidgets.QLabel(self.trainingTab)
        self.EPlabel.setGeometry(QtCore.QRect(680, 560, 60, 20))
        self.EPlabel.setObjectName("EPlabel")
        self.epochEdit.setText("20")


        self.targetgraphicsView = QtWidgets.QGraphicsView(self.detectionTab)
        self.targetgraphicsView.setGeometry(QtCore.QRect(30, 30, 591, 561))
        self.targetgraphicsView.setObjectName("targetgraphicsView")
        
        self.detectionScene=QGraphicsScene(self.targetgraphicsView)
        self.targetgraphicsView.setScene(self.detectionScene)
        self.dpix=QtGui.QPixmap("2.png")
        self.detectionScene.addPixmap(self.dpix)
        self.detectionScene.setSceneRect(0, 0, self.dpix.width(), self.dpix.height())
        self.detectionScene.update()


        self.lastSelectedMarkerKey=-1
        self.algorithm=0
        self.dataset=GenDataSet(1000,"./train",[100,100],self.progressBar,self.trainButton)
        self.threadpool = QThreadPool()
        self.mldetection=None
        self.retranslateUi(self)
        
    def changeAlgorithm(self):
        self.algorithm=self.algComboBox.currentIndex()
    
    
    def tableClicked(self, clickedIndex):
        row=clickedIndex.row()
        key = self.markerTmodel.data(self.markerTmodel.index(row, 0))
        if  int(self.lastSelectedMarkerKey)>-1:
            self.imageScene.disableSelectedMarker(self.lastSelectedMarkerKey)
            self.imageScene.enableSelectedMarker(key)
        else:
            self.imageScene.enableSelectedMarker(key)
        self.lastSelectedMarkerKey=key
        

    def addMarker(self):
        marker=self.imageScene.updateLastMarker()
        if marker==False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please select marker from the picture")
            msg.setInformativeText("Use mouse left click and drag to select a marker.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        self.markerTmodel.appendRow(marker)
    def removeMarker(self):
        selection=self.markerTable.selectionModel().selectedRows()
        if len(selection)==0:
            return
        index = selection[0]
        row = index.row()
        key = self.markerTmodel.data(self.markerTmodel.index(row, 0))
        self.imageScene.removeSelectedMarker(key)
        self.markerTmodel.removeRow(row)
        self.lastSelectedMarkerKey=-1

    def startTraining(self):
        self.dataset=GenDataSet(1000,"./train",[100,100],self.progressBar,self.trainButton)
        markerpixs=self.imageScene.getSetlectedMarkers()
        self.dataset.setImages(markerpixs)
        self.dataset.setModelType(self.algorithm)
        self.dataset.setEpochs(int(self.epochEdit.text()))
        self.threadpool.start(self.dataset) 

    def detect(self):  
        image_name=self.srcImageEdit.text()
        if not os.path.isfile(image_name):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please give a valid image file name")
            msg.setInformativeText("Use select to browse a file.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        self.detectPushButton.setEnabled(False)

        dir_name=self.outputEdit.text()
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        self.mldetection=MLDetection(learning_width=self.dataset.dia_len,out_dir=dir_name)
        image=cv2.imread(image_name)
        self.mldetection.process(image)
        detImage=self.mldetection.getProcessedImage()
        height, width, channel = detImage.shape
        bytesPerLine = 3 * width
        qImg = QImage(detImage.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.detectionScene.clear()
        self.detectionScene.addPixmap(QtGui.QPixmap.fromImage(qImg))

        QtWidgets.QApplication.restoreOverrideCursor()
        self.detectPushButton.setEnabled(True)
        print ("Complted detection")


    def openDetectFile(self):
        
        fileName, _ = QFileDialog.getOpenFileName(self,"Open file")
        if fileName:
            self.srcImageEdit.setText(fileName)
            self.dpix=QtGui.QPixmap(fileName)
            self.detectionScene.clear()
            self.detectionScene.addPixmap(self.dpix)
            self.detectionScene.setSceneRect(0, 0, self.dpix.width(), self.dpix.height())
            
    
    def openInputFile(self):
        
        fileName, _ = QFileDialog.getOpenFileName(self,"Open file")
        if fileName:
            self.InputlineEdit.setText(fileName)
            self.spix=QtGui.QPixmap(fileName)
            self.imageScene.removeAllItems()
            self.imageScene.setImage(self.spix)
            self.markerTmodel.clear()
            self.srcImageEdit.setText(fileName)
            self.dpix=QtGui.QPixmap(fileName)
            self.detectionScene.clear()
            self.detectionScene.addPixmap(self.dpix)
            self.detectionScene.setSceneRect(0, 0, self.dpix.width(), self.dpix.height())
           


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Markers"))
        self.inputSelectButton.setText(_translate("MainWindow", "Select"))
        self.trainButton.setText(_translate("MainWindow", "Start Training"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Marker Selection"))
        self.markerAddButton.setText(_translate("MainWindow", "ADD"))
        self.markerDelButton.setText(_translate("MainWindow", "DELETE"))
        self.label_4.setText(_translate("MainWindow", "Selected Area"))
        self.algLabel.setText(_translate("MainWindow", "Algorithm"))
        self.trainingTab_2.setTabText(self.trainingTab_2.indexOf(self.trainingTab), _translate("MainWindow", "Training"))
        self.trainingTab_2.setTabText(self.trainingTab_2.indexOf(self.detectionTab), _translate("MainWindow", "Detection"))
        self.label.setText(_translate("MainWindow", "Output Directory"))
        self.label_4.setText(_translate("MainWindow", "Source Image"))
        self.srcSelectButton.setText(_translate("MainWindow", "Select"))
        self.detectPushButton.setText(_translate("MainWindow", "Detect"))
        self.EPlabel.setText(_translate("MainWindow", "Epochs"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    ui = Ui_MainWindow()
    
    ui.show()
    sys.exit(app.exec_())

