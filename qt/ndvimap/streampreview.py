from PyQt4.QtGui import QWidget, QHBoxLayout, QLabel, QPixmap, QTransform
from PyQt4.QtCore import Qt

class StreamPreviewWidget(QWidget):
    def __init__(self, list_of_files):
        QWidget.__init__(self)
        l1 = QHBoxLayout(self)
        k = 0;
        n = 0;
        for fileName in list_of_files:
            if k < 10 and n == 0: 
                label = QLabel()
                l1.addWidget(label)
                pixmap = QPixmap(fileName)
                pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio)
                pixmap = pixmap.transformed(QTransform().rotate(180))
                label.setPixmap(pixmap)
            n = n + 1
            if n == len(list_of_files) / 10:
                k = k + 1
                n = 0
    def mousePressEvent(self, event):   
        x = 1.0 * event.x() / self.panel.width() * len(self.panel.list_of_files)
        self.panel.update(int(x))
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            print "Simple mouse motion"
        elif event.buttons() == Qt.LeftButton:
            x = 1.0 * event.x() / self.panel.width() * len(self.panel.list_of_files)
            self.panel.update(int(x))
        elif event.buttons() == Qt.RightButton:
            print "Right click drag"
    def setPanel(self, panelWidget):
        self.panel = panelWidget;