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
    print tmp
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    
    if tmp == "sin":
        y1 = np.sin(2 * np.pi * x1) * np.exp(-x1)
        y2 = np.sin(2 * np.pi * x2)
        w1 = pg.PlotWidget(title=tmp+" Wave")
        w1.plot(x2,y2)
        ui.dockWidget.setWidget(w1)
    elif tmp == "cos":
        y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
        y2 = np.cos(2 * np.pi * x2)
        w1 = pg.PlotWidget(title=tmp+" Wave")
        w1.plot(x2,y2)
        ui.dockWidget.setWidget(w1)
    elif tmp == "Oscillation":
        y1 = np.sin(2 * np.pi * x1) * np.exp(-x1)
        w1 = pg.PlotWidget(title=tmp+" Wave")
        w1.plot(x1,y1)
        ui.dockWidget_2.setWidget(w1)

# now bind the above functions with buttons
ui.pushButton.clicked.connect(showPlot)
ui.pushButton_2.clicked.connect(quit)

# To display main form and GUI
Form.show()
sys.exit(app.exec_())