"""
Author : Pankaj soni
"""
#######################
# NOTE: This executable is crashing sometimes, i am not able to figure out why. 
# If user of this code finds it then please post the reason. It will be highly appreciated.

from PySide import QtCore, QtGui
import sys
import threading, time
import re

import serial.tools.list_ports

from Com_Port_filter import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form
def updatePortList():
    ui.comboBox.clear()
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        itm = p[0]
        ui.comboBox.addItem(itm)    
        ui.comboBox_2.addItem(itm)    

def connectPort():
    global ser
    port = ui.comboBox_2.currentText()
    baudarate =ui.comboBox_3.currentText()
    datasize =ui.comboBox_4.currentText()
    paritybit =ui.comboBox_5.currentText()
    stopbits =ui.comboBox_6.currentText()
    flowcontrol =ui.comboBox_7.currentText()
    #~ print port,baudarate,datasize,paritybit,stopbits,flowcontrol
    
    # some values are hardcoded, however based on need it can be changed.
    ser = serial.Serial(port, baudrate=baudarate, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

def startCapturing():
    global ser
    while 1:
        tmp = ser.readline()
        #~ print tmp
        ui.textEdit.append(tmp)
        filterTxt = ui.lineEdit.text()
        #~ print "current text is!!!",filterTxt
        #~ reVar = "'(.*)("+filterTxt+" [0-9]).*'"
        reVar = filterTxt
        #~ print "reVar is::",reVar
        matchObj = re.match(reVar,tmp)
        if matchObj:
            tmp2 = matchObj.group(2)
            print tmp2
            ui.textEdit_2.append(tmp2)

# Using thread module to make this function non-blocking
def threadFunc():
    thread = threading.Thread(target=startCapturing)
    time.sleep(5)
    thread.start()
    time.sleep(2)


# now bind the above functions with buttons
ui.pushButton.clicked.connect(updatePortList)
ui.pushButton_2.clicked.connect(connectPort)
ui.pushButton_3.clicked.connect(quit)
ui.pushButton_4.clicked.connect(threadFunc)

# To display main form and GUI
    
Form.show()
sys.exit(app.exec_())

