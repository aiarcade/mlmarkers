# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.trainingTab_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.trainingTab_2.setGeometry(QtCore.QRect(50, 20, 881, 641))
        self.trainingTab_2.setObjectName("trainingTab_2")
        self.trainingTab = QtWidgets.QWidget()
        self.trainingTab.setObjectName("trainingTab")
        self.trainingTab_2.addTab(self.trainingTab, "")
        self.detectionTab = QtWidgets.QWidget()
        self.detectionTab.setObjectName("detectionTab")
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
        self.trainingTab_2.addTab(self.detectionTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.trainingTab_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ML Markers"))
        self.trainingTab_2.setTabText(self.trainingTab_2.indexOf(self.trainingTab), _translate("MainWindow", "Training"))
        self.label.setText(_translate("MainWindow", "Output Directory"))
        self.label_4.setText(_translate("MainWindow", "Source Image"))
        self.srcSelectButton.setText(_translate("MainWindow", "Select"))
        self.detectPushButton.setText(_translate("MainWindow", "Detect"))
        self.trainingTab_2.setTabText(self.trainingTab_2.indexOf(self.detectionTab), _translate("MainWindow", "Detection"))

import ml_rc
