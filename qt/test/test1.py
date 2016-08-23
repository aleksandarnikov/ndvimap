import os
import sys
from PyQt4.QtGui import *
 
# Create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("PyQT4 Pixmap @ pythonspot.com ") 
 
# Create widget
label = QLabel(w)
pixmap = QPixmap("c:\\local\\agro\\testsample\\thermal\\20160719_080017.jpg")
label.setPixmap(pixmap)
w.resize(pixmap.width(),pixmap.height())
 
# Draw window
w.show()
app.exec_()