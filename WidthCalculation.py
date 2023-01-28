# Main program

import sys
from PyQt5 import  QtGui 
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt

from widthUICalculation import Ui_MainWindow
from ImageViewer import leftImagePhotoViewer

class Window(QMainWindow):
    def __init__(self):
        
        super(Window, self).__init__()
        self.chosen_points = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.openFolderButton.clicked.connect(self.loadImage)
        #self.ui.previousImageButton.clicked.connect(self.previousImage)
        #self.ui.nextImageButton.clicked.connect(self.nextImage) 
                
        #rightimageviwer
        self.viewer2 = leftImagePhotoViewer(self)
        self.ui.rightZoomInButton.clicked.connect(self.zoom_in2)
        self.ui.rightZoomOutButton.clicked.connect(self.zoom_out2) 
        self.ui.trackCrackWidthButton.clicked.connect(self.paintRight)
        self.ui.trackCrackWidthButton.setCheckable(True)
          
        
        self.pixmap = QtGui.QImage("picture.png")
        self.pixmap.fill(Qt.white) 
        buttonsignal = 0
        
        #calculate right viewer
        self.ui.calculateCrackWidthButton.clicked.connect(self.calculateRight) 
        self.line1 =1
        self.row1=0
        self.data1 =[]
        self.dimensions1 = 0
        
        
    def calculateRight(self):
        self.data1.clear()
        distance = self.ui.distanceLineEdit.text()

        print(len(self.viewer2.objects))
        for i in self.viewer2.objects:
            print(i)
            if i == 'x':
                self.data1.append({"line":str(self.line1),"distance": str(self.dimensions1)})
                self.line1=self.line1+1
                self.dimensions1 = 0
                
            else:      
                dimension=(0.00099*float(distance) + 0.00142)*float(i)
                dimension = round(dimension, 4)
                print(dimension)
                self.dimensions1 = self.dimensions1 + dimension
               
        self.ui.crackWidthTableWidget.setRowCount(self.line1)
        for x in self.data1:
            self.ui.crackWidthTableWidget.setItem(self.row1,0,QTableWidgetItem(x["line"]))
            self.ui.crackWidthTableWidget.setItem(self.row1,1,QTableWidgetItem(x["distance"]))
            self.row1=self.row1+1
        self.viewer2.objects.clear()
        
    def paintRight(self):
        if self.ui.trackCrackWidthButton.isChecked():
            buttonsignal1 = 1
            self.viewer2.paint(buttonsignal1)
            self.ui.trackCrackWidthButton.setText("Done")
            self.ui.calculateCrackWidthButton.setEnabled(False)
            
        else:
            buttonsignal1 = 0
            self.viewer2.paint(buttonsignal1)
            self.ui.trackCrackWidthButton.setText("Trace Crack Width")
            self.ui.calculateCrackWidthButton.setEnabled(True)
            
               

    def loadImage(self):
        filename = QFileDialog.getOpenFileNames(self, "Open File")
        self.image = filename[0]
        self.x=0
        self.y=len(self.image)-1
        self.pixmap = QImage(self.image[self.x])
        self.viewer2.setPhoto(self.pixmap)
        
    def zoom_in2(self):
        self.viewer2.on_zoom_in()
        
    def zoom_out2(self):
        self.viewer2.on_zoom_out()
    
    def nextImage(self):
        self.x+=1
        self.pixmap = QImage(self.image[self.x])
        self.viewer2.setPhoto(self.pixmap)
    
    def previousImage(self):
        self.x-=1
        self.pixmap = QImage(self.image[self.x])
        self.viewer2.setPhoto(self.pixmap)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
