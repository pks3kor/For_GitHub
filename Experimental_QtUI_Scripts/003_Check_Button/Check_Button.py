# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Check_Button.ui'
#
# Created: Fri Jun 09 15:47:43 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(216, 88)
        self.formLayoutWidget = QtGui.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 20, 172, 42))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkBox = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_3 = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBox_4)
        self.checkBox_2 = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.checkBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "CheckBox_1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "CheckBox_3", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Form", "CheckBox_4", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "CheckBox_2", None, QtGui.QApplication.UnicodeUTF8))

