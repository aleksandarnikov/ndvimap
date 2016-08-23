import os
import sys
import glob
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
# Create window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("PyQT4 Pixmap @ pythonspot.com ") 


ll = QVBoxLayout(w);

w1 = QWidget()
l1 = QHBoxLayout(w1)
ll.addWidget(w1)
s = "c:\\local\\agro\\testsample\\thermal\\";
list_of_files1 = glob.glob(s + "\\*.jpg")
k = 0;
n = 0;
for fileName in list_of_files1:
    if k < 10 and n == 0: 
        label = QLabel()
        l1.addWidget(label)
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        pixmap = pixmap.transformed(QTransform().rotate(180))
        label.setPixmap(pixmap)
    n = n + 1
    if n == 10:
        k = k + 1
        n = 0
        

w2 = QWidget()
l2 = QHBoxLayout(w2)
ll.addWidget(w2)
s = "c:\\local\\agro\\testsample\\rgb\\";
list_of_files2 = glob.glob(s + "\\*.jpg")
k = 0;
n = 0;
for fileName in list_of_files2:
    if k < 10 and n == 0: 
        label = QLabel()
        l2.addWidget(label)
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
    n = n + 1
    if n == 20:
        k = k + 1
        n = 0

# Create widget
#w.resize(pixmap.width(),pixmap.height())
 
# Draw window
w.show()
app.exec_()