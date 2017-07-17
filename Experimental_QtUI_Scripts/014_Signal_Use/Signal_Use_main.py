"""
Author : Pankaj soni
"""
#######################
# NOTE: This executable is crashing sometimes, i am not able to figure out why. 
# If user of this code finds it then please post the reason. It will be highly appreciated.

from PySide import QtCore, QtGui
import sys
import threading, time

import serial.tools.list_ports

from Signal_Use import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form

# To display main form and GUI
    
Form.show()
sys.exit(app.exec_())

