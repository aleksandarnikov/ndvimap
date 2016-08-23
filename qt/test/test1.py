import os
import sys
import glob
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
 
class MyWidget(QWidget):
    def mousePressEvent(self, event):   
        print self.panel.width()
        print event.x()
        print len(self.panel.list_of_files)
        x = 1.0 * event.x() / self.panel.width() * len(self.panel.list_of_files)
        print x
        self.panel.update(int(x))
    def setPanel(self, panelWidget):
        self.panel = panelWidget;
        
 
class PanelWidget(QWidget):
    firstcall = 1;
    def __init__(self, list_of_files):
        QWidget.__init__(self)
        self.list_of_files = list_of_files
    def update(self, index):
        if self.firstcall == 0:
            self.layout().removeWidget(self.child)
            self.child.setParent(None)
        self.firstcall = 0
        self.child = QLabel()
        pixmap = QPixmap(self.list_of_files[index])
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio)
        self.child.setPixmap(pixmap)
        self.layout().addWidget(self.child)
    
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
    if n == len(list_of_files1) / 10:
        k = k + 1
        n = 0
        

w2 = MyWidget()
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
    if n == len(list_of_files2) / 10:
        k = k + 1
        n = 0

w3 = PanelWidget(list_of_files2)
l3 = QHBoxLayout(w3)
ll.addWidget(w3)
w3.update(0)
w2.setPanel(w3)

# Create widget
#w.resize(pixmap.width(),pixmap.height())
 
# Draw window
w.show()
app.exec_()