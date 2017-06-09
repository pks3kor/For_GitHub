"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys

from Check_Button import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form
def checkStatus():
    if ui.checkBox.isChecked() == True:
        print "checkBox is clicked"
    elif ui.checkBox_2.isChecked() == True:
        print "checkBox_2 is clicked"
    elif ui.checkBox_3.isChecked() == True:
        print "checkBox_3 is clicked"
    elif ui.checkBox_4.isChecked() == True:
        print "checkBox_4 is clicked"


# now bin the above functions with buttons
ui.checkBox.clicked.connect(checkStatus)
ui.checkBox_2.clicked.connect(checkStatus)
ui.checkBox_3.clicked.connect(checkStatus)
ui.checkBox_4.clicked.connect(checkStatus)


# To display main form and GUI
Form.show()
sys.exit(app.exec_())