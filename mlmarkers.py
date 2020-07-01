

from PyQt5 import QtCore, QtGui, QtWidgets
from selectionarea import SelectionArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from multiprocessing import Process
from generatedataset import GenDataSet
from status import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(919, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(200, 20, 91, 41))
        self.pushButton.setObjectName("pushButton")
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
        self.trainButton.setGeometry(QtCore.QRect(750, 570, 113, 32))
        self.trainButton.setObjectName("trainButton")
        
        self.trainingTab_2.addTab(self.trainingTab, "")
        self.detectionTab = QtWidgets.QWidget()
        self.detectionTab.setObjectName("detectionTab")
        self.trainingTab_2.addTab(self.detectionTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.trainingTab_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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


        self.progressBar = QtWidgets.QProgressBar(self.trainingTab)
        self.progressBar.setGeometry(QtCore.QRect(600, 570, 100, 21))
        self.progressBar.setProperty("value",0)
        self.progressBar.setObjectName("progressBar")
        self.algComboBox = QtWidgets.QComboBox(self.trainingTab)
        self.algComboBox.setGeometry(QtCore.QRect(615, 10, 250, 26))
        self.algComboBox.setObjectName("algComboBox")
        self.algComboBox.addItem("CNN")
        self.algComboBox.addItem("SVM")
        self.algLabel = QtWidgets.QLabel(self.trainingTab)
        self.algLabel.setGeometry(QtCore.QRect(550, 10, 91, 21))
        self.algLabel.setObjectName("algLabel")

        self.targetgraphicsView = QtWidgets.QGraphicsView(self.detectionTab)
        self.targetgraphicsView.setGeometry(QtCore.QRect(30, 30, 591, 561))
        self.targetgraphicsView.setObjectName("targetgraphicsView")
        self.OutpulineEdit = QtWidgets.QLineEdit(self.detectionTab)
        self.OutpulineEdit.setGeometry(QtCore.QRect(640, 200, 211, 21))
        self.OutpulineEdit.setObjectName("OutpulineEdit")
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





        self.lastSelectedMarkerKey=-1
        self.dataset=GenDataSet(1000,"./train",[100,100],self.progressBar,self.trainButton)
        self.threadpool = QThreadPool()
        self.retranslateUi(MainWindow)
        
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
        markerpixs=self.imageScene.getSetlectedMarkers()
        self.dataset.setImages(markerpixs)
        self.threadpool.start(self.dataset) 




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Markers"))
        self.pushButton.setText(_translate("MainWindow", "Select"))
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

