# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spin_Box.ui'
#
# Created: Wed Jun 28 18:41:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(110, 50, 161, 16))
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 90, 161, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 90, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 191, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 30, 191, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "SpinBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "DoubleSpinBox", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "getVal", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "getVal", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Current val in spin box:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Current val in double spin box:", None, QtGui.QApplication.UnicodeUTF8))

