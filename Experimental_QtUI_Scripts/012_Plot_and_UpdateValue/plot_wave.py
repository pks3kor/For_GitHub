# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_wave.ui'
#
# Created: Thu Jul 13 18:42:09 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(849, 568)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 81, 22))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(10, 160, 621, 341))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.dockWidget_2 = QtGui.QDockWidget(self.splitter)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        self.dockWidget = QtGui.QDockWidget(self.splitter)
        self.dockWidget.setAcceptDrops(True)
        self.dockWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dockWidget.setAutoFillBackground(True)
        self.dockWidget.setFloating(False)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(170, 80, 251, 52))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dial = QtGui.QDial(self.widget)
        self.dial.setMinimum(5)
        self.dial.setMaximum(200)
        self.dial.setSingleStep(5)
        self.dial.setObjectName("dial")
        self.horizontalLayout.addWidget(self.dial)
        self.dial_2 = QtGui.QDial(self.widget)
        self.dial_2.setMinimum(100)
        self.dial_2.setMaximum(20000)
        self.dial_2.setSingleStep(100)
        self.dial_2.setObjectName("dial_2")
        self.horizontalLayout.addWidget(self.dial_2)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("valueChanged(int)"), self.pushButton.click)
        QtCore.QObject.connect(self.dial_2, QtCore.SIGNAL("valueChanged(int)"), self.pushButton.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Show_Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "sin & cos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_2.setWindowTitle(QtGui.QApplication.translate("Form", "CosWave", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("Form", "SinWave", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Amplitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Frequency", None, QtGui.QApplication.UnicodeUTF8))

