from PyQt4.QtGui import QWidget, QLabel, QPixmap, QHBoxLayout
from PyQt4.QtCore import Qt

class PanelWidget(QWidget):
    firstcall = 1;
    def __init__(self, list_of_files):
        QWidget.__init__(self)
        self.list_of_files = list_of_files
        QHBoxLayout(self)
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