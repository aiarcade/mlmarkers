

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from queue import Queue
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TextReceiver(QObject):
    textsignal = pyqtSignal(str)

    def __init__(self,queue,*args,**kwargs):
        QObject.__init__(self,*args,**kwargs)
        self.queue = queue

    @pyqtSlot()
    def run(self):
        while True:
            text = self.queue.get()
            self.textsignal.emit(text)

class WriteStream(object):
    def __init__(self,queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)
    def flush(self):
        pass

class StatusWidget(QtWidgets.QWidget):

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setObjectName("Form")
        self.resize(602, 269)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(40, 230, 511, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.cosnoleEdit = QtWidgets.QTextEdit(self)
        self.cosnoleEdit.setGeometry(QtCore.QRect(40, 20, 511, 201))
        self.cosnoleEdit.setObjectName("cosnoleEdit")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Training", "Training"))

    @pyqtSlot(str)
    def append_text(self,text):
        self.cosnoleEdit.moveCursor(QTextCursor.End)
        self.cosnoleEdit.insertPlainText( text )


