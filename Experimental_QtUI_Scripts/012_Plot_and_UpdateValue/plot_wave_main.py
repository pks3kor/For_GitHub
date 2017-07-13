"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

from plot_wave import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form

def showPlot():
    tmp = ui.comboBox.currentText()
    #~ print tmp

    #~ Fs = 8000
    Fs = ui.dial_2.value()
    f = 5
    #~ sample = 8000
    sample = ui.dial_2.value()
    x = np.arange(sample)
    amp = ui.dial.value()
    
    # For sin
    y = np.sin(amp * np.pi * f * x / Fs)
    w1 = pg.PlotWidget(title="Sin Wave")
    w1.plot(x,y)
    ui.dockWidget.setWidget(w1)
    
    # For cos
    y2 = np.cos(amp * np.pi * f * x / Fs)
    w2 = pg.PlotWidget(title="Cos Wave")
    w2.plot(x,y2)
    ui.dockWidget_2.setWidget(w2)

# now bind the above functions with buttons
ui.pushButton.clicked.connect(showPlot)
ui.pushButton_2.clicked.connect(quit)

# To display main form and GUI
Form.show()
sys.exit(app.exec_())