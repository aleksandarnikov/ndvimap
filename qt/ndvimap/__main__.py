
import sys
import glob
from PyQt4.QtGui import QApplication
from mainwindow import NDVIWindow
from streampreview import StreamPreviewWidget
from panelwidget import PanelWidget

app = QApplication(sys.argv)
w = NDVIWindow()

s = "c:\\local\\agro\\testsample\\thermal\\";
list_of_files1 = glob.glob(s + "\\*.jpg")
previewWidget1 = StreamPreviewWidget(list_of_files1)
w.addComponent(previewWidget1)


panelWidget1 = PanelWidget(list_of_files1)
previewWidget1.setPanel(panelWidget1)
w.addComponent(panelWidget1)
panelWidget1.update(0)


s = "c:\\local\\agro\\testsample\\rgb\\";
list_of_files2 = glob.glob(s + "\\*.jpg")
previewWidget2 = StreamPreviewWidget(list_of_files2)
w.addComponent(previewWidget2)

panelWidget2 = PanelWidget(list_of_files2)
previewWidget2.setPanel(panelWidget2)
w.addComponent(panelWidget2)
panelWidget2.update(0)


# Draw window
w.show()
app.exec_()