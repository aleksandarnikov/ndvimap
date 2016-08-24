from PyQt4.QtGui import QWidget, QVBoxLayout

class NDVIWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("NDVI Map") 
        self.l = QVBoxLayout(self);
    def addComponent(self, widget):
        self.l.addWidget(widget)
        