"""
Author : Pankaj soni
"""

from PySide import QtCore, QtGui
import sys

from Text_Edit import Ui_Form

# Initialize main GUI and use its resources
app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

#############################
# Write your own function here and bind them with buttons usied in GUI form
def sayHello():
    print "Hello there!!!"

def clearText():
    ui.textEdit.clear()

def getText():
    tmp = ui.textEdit.toPlainText()
    print tmp

# now bind the above functions with buttons
ui.pushButton.clicked.connect(getText)
ui.pushButton_2.clicked.connect(quit)
ui.pushButton_3.clicked.connect(clearText)


# To display main form and GUI
Form.show()
sys.exit(app.exec_())