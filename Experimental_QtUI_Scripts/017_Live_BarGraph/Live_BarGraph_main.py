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
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import serial.tools.list_ports

from Live_BarGraph import Ui_Form

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

global b_num,x,y1,y2,y3,y4
y1,y2,y3,y4 = [],[],[],[]
x = np.arange(5)
w1 = pg.PlotWidget(title="Detection Statistics")
def buttonStatitics(button_num):    
    global b_num,x,y1,y2,y3,y4
    if button_num == "1":
        y1.append(1)
        bg1 = pg.BarGraphItem(x=x, height=len(y1), width=.4, brush='r')
        w1.addItem(bg1)
    elif button_num == "2":
        y2.append(2)
        bg2 = pg.BarGraphItem(x=x, height=len(y2), width=.4, brush='g')
        w1.addItem(bg2)
    elif button_num == "3":
        y3.append(3)
        bg3 = pg.BarGraphItem(x=x, height=len(y3), width=.4, brush='b')
        w1.addItem(bg3)
    elif button_num == "4":
        y4.append(4)
        bg4 = pg.BarGraphItem(x=x, height=len(y4), width=.4, brush='y')
        w1.addItem(bg4)
    elif len(y1) and len(y2) and len(y3) and len(y4) == 0:
        bg1 = pg.BarGraphItem(x=x, height=0, width=.4, brush='r')
        bg2 = pg.BarGraphItem(x=x, height=0, width=.4, brush='g')
        bg3 = pg.BarGraphItem(x=x, height=0, width=.4, brush='b')
        bg4 = pg.BarGraphItem(x=x, height=0, width=.4, brush='y')
        w1.addItem(bg1)
        w1.addItem(bg2)
        w1.addItem(bg3)
        w1.addItem(bg4)
    ui.dockWidget.setWidget(w1)
    ui.label_8.setText("Button_1:: "+str(len(y1)))
    ui.label_9.setText("Button_2:: "+str(len(y2)))
    ui.label_10.setText("Button_3:: "+str(len(y3)))
    ui.label_11.setText("Button_4:: "+str(len(y4)))
    #~ print "length of Y1:: ",len(y1)
    #~ print "length of Y2:: ",len(y2)
    #~ print "length of Y3:: ",len(y3)
    #~ print "length of Y4:: ",len(y4)

def startCapturing():
    global ser,b_num
    tmp = ser.readline()
    #~ print tmp
    ui.textEdit.append(tmp)
    filterTxt = ui.lineEdit.text()
    reVar = filterTxt
    #~ print "reVar is::",reVar
    matchObj = re.match(reVar,tmp)
    if matchObj:
        tmp2 = matchObj.group(2)
        #~ print tmp2[-1]
        b_num = tmp2[-1]
        #~ print b_num
        buttonStatitics(b_num)
        ui.textEdit_2.append(tmp2)

# Using thread module to make this function non-blocking
timer = QtCore.QTimer()
def showUpdate():
    global timer,b_num
    timer.timeout.connect(startCapturing)
    timer.start(20)


# now bind the above functions with buttons
ui.pushButton.clicked.connect(updatePortList)
ui.pushButton_2.clicked.connect(connectPort)
ui.pushButton_3.clicked.connect(quit)
ui.pushButton_4.clicked.connect(showUpdate)

# To display main form and GUI
    
Form.show()
sys.exit(app.exec_())

