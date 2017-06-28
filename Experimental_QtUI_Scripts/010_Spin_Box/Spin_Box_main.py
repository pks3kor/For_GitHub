"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys

from Spin_Box import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form
def getSpinBoxVal():
    tmp = ui.spinBox.value()
    ui.label_3.setText("Current val in spin box: "+str(tmp))     #Display current value in label
    #~ print tmp

def getDoubleSpinBoxVal():
    tmp = ui.doubleSpinBox.value()
    ui.label_4.setText("Current val in double spin box: "+str(tmp))     #Display current value in label
    #~ print tmp

# now bind the above functions with buttons
ui.pushButton.clicked.connect(getSpinBoxVal)
ui.pushButton_2.clicked.connect(getDoubleSpinBoxVal)
ui.pushButton_3.clicked.connect(quit)

# To display main form and GUI
Form.show()
sys.exit(app.exec_())