

from PyQt5 import QtCore, QtGui, QtWidgets
from selectionarea import SelectionArea
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        self.imageScene.setImage(QtGui.QPixmap("1.png"))
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

        self.retranslateUi(MainWindow)
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

        self.lastSelectedMarkerKey=-1
        
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
        pass



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Markers"))
        self.pushButton.setText(_translate("MainWindow", "Select"))
        self.trainButton.setText(_translate("MainWindow", "Start Training"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Marker Selection"))
        self.markerAddButton.setText(_translate("MainWindow", "ADD"))
        self.markerDelButton.setText(_translate("MainWindow", "DELETE"))
        self.label_4.setText(_translate("MainWindow", "Selected Area"))
        
        self.trainingTab_2.setTabText(self.trainingTab_2.indexOf(self.trainingTab), _translate("MainWindow", "Training"))
        self.trainingTab_2.setTabText(self.trainingTab_2.indexOf(self.detectionTab), _translate("MainWindow", "Detection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

