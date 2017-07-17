# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signal_Use.ui'
#
# Created: Mon Jul 17 17:49:54 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(849, 568)
        self.dial = QtGui.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(90, 210, 50, 64))
        self.dial.setObjectName("dial")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 200, 46, 13))
        self.label.setObjectName("label")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(230, 36, 211, 411))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.lcdNumber = QtGui.QLCDNumber(self.splitter)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalSlider = QtGui.QSlider(self.splitter)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalScrollBar = QtGui.QScrollBar(self.splitter)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.progressBar = QtGui.QProgressBar(self.splitter)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtGui.QSlider(self.splitter)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalScrollBar = QtGui.QScrollBar(self.splitter)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.lcdNumber.display)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.progressBar.setValue)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.horizontalScrollBar.setValue)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.verticalSlider.setValue)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.verticalScrollBar.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Rotate_It", None, QtGui.QApplication.UnicodeUTF8))

