"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys

from Tab_View import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form
def sayHello():
    print "Hello there!!!"

# now bin the above functions with buttons
ui.pushButton.clicked.connect(sayHello)
ui.pushButton_2.clicked.connect(quit)

# To display main form and GUI
Form.show()
sys.exit(app.exec_())