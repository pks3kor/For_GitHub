"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys

from Radio_Button import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form
def checkStatus():
    if ui.radioButton.isChecked() == True:
        print "radioButton_1 is clicked"
    else :
        print "radioButton_2 is clicked"

# now bind the above functions with buttons
ui.radioButton.clicked.connect(checkStatus)
ui.radioButton_2.clicked.connect(checkStatus)

# To display main form and GUI
Form.show()
sys.exit(app.exec_())