"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys,random

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import threading, time

from Auto_Update_Plot import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form

def showPlot():
    tmp = random.randint(1, 10)
    x1 = np.linspace(0.0, tmp)
    tmp2 = tmp = random.randint(1, 10)
    y1 = np.sin(2 * np.pi * x1)
    w1 = pg.PlotWidget()
    w1.plot(x1,y1)
    w1.plot(x1,y1+5)
    ui.dockWidget.setWidget(w1)

# To update the graph 
# the update() slot is called every 50 millisecond.
timer = QtCore.QTimer()
def showUpdate():
    global timer
    timer.timeout.connect(showPlot)
    timer.start(50)

# now bind the above functions with buttons
ui.pushButton.clicked.connect(showUpdate)
ui.pushButton_2.clicked.connect(quit)

# To display main form and GUI
Form.show()
sys.exit(app.exec_())