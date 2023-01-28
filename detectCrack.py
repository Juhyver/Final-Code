# Main program
import sys
import os
import cv2
import math
import numpy as np
import scipy.ndimage
from pathlib import Path
from PyQt5 import  QtGui 
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QPixmap, qRgb
from PyQt5.QtCore import Qt


from widthUICalculation import Ui_MainWindow
from ImageViewer import leftImagePhotoViewer



def orientated_non_max_suppression(mag, ang):
    ang_quant = np.round(ang / (np.pi/4)) % 4
    winE = np.array([[0, 0, 0],[1, 1, 1], [0, 0, 0]])
    winSE = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    winS = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
    winSW = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    magE = non_max_suppression(mag, winE)
    magSE = non_max_suppression(mag, winSE)
    magS = non_max_suppression(mag, winS)
    magSW = non_max_suppression(mag, winSW)

    mag[ang_quant == 0] = magE[ang_quant == 0]
    mag[ang_quant == 1] = magSE[ang_quant == 1]
    mag[ang_quant == 2] = magS[ang_quant == 2]
    mag[ang_quant == 3] = magSW[ang_quant == 3]
    return mag

def non_max_suppression(data, win):
    data_max = scipy.ndimage.filters.maximum_filter(data, footprint=win, mode='constant')
    data_max[data != data_max] = 0
    return data_max




class Window(QMainWindow):
    def __init__(self):
        
        super(Window, self).__init__()
        self.chosen_points = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.openFolderButton.clicked.connect(self.loadImage)
        self.ui.detectCrackButton.clicked.connect(self.detectCrack)
                
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
        self.ui.calculateCrackWidthButton.clicked.connect(self.calculate) 
        self.line1 =1
        self.row1=0
        self.data1 =[]
        self.dimensions1 = 0

        # start calulcation
        self.gray_image = None
    
    def gray(self):
        self.gray_image = cv2.imread(self.image, 0)
        with_nmsup = True #apply non-maximal suppression
        fudgefactor = 1.3 #with this threshold you can play a little bit
        sigma = 21 #for Gaussian Kernel
        kernel = 2*math.ceil(2*sigma)+1 #Kernel size

        gray_image = self.gray_image/255.0
        blur = cv2.GaussianBlur(gray_image, (kernel, kernel), sigma)
        gray_image = cv2.subtract(gray_image, blur)

        # compute sobel response
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        mag = np.hypot(sobelx, sobely)
        ang = np.arctan2(sobely, sobelx)

        # threshold
        threshold = 4 * fudgefactor * np.mean(mag)
        mag[mag < threshold] = 0

        #either get edges directly
        if with_nmsup is False:
            mag = cv2.normalize(mag, 0, 255, cv2.NORM_MINMAX)
            kernel = np.ones((5,5),np.uint8)
            result = cv2.morphologyEx(mag, cv2.MORPH_CLOSE, kernel)

        #or apply a non-maximal suppression
        else:
            # non-maximal suppression
            mag = orientated_non_max_suppression(mag, ang)
            # create mask
            mag[mag > 0] = 255
            mag = mag.astype(np.uint8)

            kernel = np.ones((5,5),np.uint8)
            result = cv2.morphologyEx(mag, cv2.MORPH_CLOSE, kernel)


        
        self.detectPhoto = result
        filename = os.path.basename(self.image)
        path = os.path.dirname(self.image)
        self.dir = path + "/gry_"+filename
        print(self.dir)
        cv2.imwrite(self.dir,self.detectPhoto)

        
    def calculate(self):
        self.data1.clear()
        #distance = self.ui.distanceLineEdit.text()

        print(len(self.viewer2.objects))
        for i in self.viewer2.objects:
            print(i)
            if i == 'x':
                self.data1.append({"line":str(self.line1),"distance": str(self.dimensions1)})
                self.line1=self.line1+1
                self.dimensions1 = 0
                
            else:      
                dimension=float(i)
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
        filename = QFileDialog.getOpenFileName()#self, "Open File")
        self.image = filename[0]
        self.pixmap = QPixmap(self.image)
        self.gray_img = cv2.imread(self.image, 0)
        cval = 10/604.6517708
        self.viewer2.setPhoto(self.pixmap,cval,self.gray_img)

    def detectCrack(self):
        self.gray_image = self.image
        self.gray()
        print("-----")
        print(self.dir)
        cval= 10/604.119412
        print(self.dir)
        self.pixmap = QPixmap(self.dir)
        self.viewer2.setPhoto(self.pixmap,cval)
        
    def detectCrack2(self):
        #Call your function to detect
        cval = 10/604.119412
        self.pixmap = QPixmap(self.dir)
        self.viewer2.setPhoto(self.pixmap,cval)
        
    def zoom_in2(self):
        self.viewer2.on_zoom_in()
        
    def zoom_out2(self):
        self.viewer2.on_zoom_out()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
