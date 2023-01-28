# Main program

import secrets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsView, QGraphicsObject, QGraphicsSceneMouseEvent
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtGui import QPen, QBrush, QColor, qRgb
from cv2 import sqrt


class leftImagePhotoViewer(QtWidgets.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):
        super(leftImagePhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        #self.ui.leftLayout.addWidget(self.ui.leftImageLabel)
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setGeometry(QtCore.QRect(40, 100, 739, 427)) 
        self.path = QtGui.QPainterPath()
        self.flag = False
        self.pixmap = QtGui.QImage("picture.png")
        #self.pixmap.fill(Qt.white)
        self.objects = []
        self.posprev = ""
        self.setSceneRect(20, 90, 451, 421)
        self.setMouseTracking(True)
        self.posprev = ""
        self.bsignal = 0
        self.count =1
        self.points = []

    def paint(self,buttonsignal):
        self.bsignal = buttonsignal
        if buttonsignal ==1:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif buttonsignal == 0:
            self.objects.append(str('x'))
            if not self.posprev:
                print("Exit Trace")
            else:
                text=self._scene.addText("Trace"+str(self.count))
                text.setDefaultTextColor(QColor(Qt.green))
                text.setPos(self.posprev.x()-50,self.posprev.y()-50)
                self.count = self.count+1    
            #self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self.posprev = ""
    
    def mouseReleaseEvent(self,event):
        size = 2
        if self.bsignal == 1:
            pos = self.mapToScene(event.pos())
            if not self.posprev:
                point = self._scene.addEllipse(-size/2,-size/2 , size, size, QPen(Qt.black), QBrush(Qt.green))
                point.setPos(pos)
                self.posprev=pos
        
            else:
                point = self._scene.addEllipse(-size/2,-size/2 , size, size, QPen(Qt.black), QBrush(Qt.green))
                point.setPos(pos)
                line = self._scene.addLine(pos.x(),pos.y(), self.posprev.x(), self.posprev.y(), QPen(Qt.green))
                self.x1 = pos.x()
                self.x2 = self.posprev.x()
                self.y1 = pos.y()
                self.y2 = self.posprev.y()
                self.distance = (((self.x1-self.x2)**2+(self.y1-self.y2)**2)**(1/2))
                print(self.distance)
                self.get_line()
                print(self.distance)
                self.objects.append(self.distance)
                self.posprev=pos
                self.points.clear()

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                self.factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(self.factor,self.factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None, cval=None, image=None):
        self._zoom = 0
        self.image = image
        self.cval = cval
        #print(self.image(0,0))
        if pixmap and not pixmap.isNull():
            self._empty = False
            #self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            #self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                self.factor = 1.25
                self._zoom += 1
            else:
                self.factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(self.factor, self.factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0
                
    def on_zoom_in(self):
        if self.hasPhoto():
            self.factor = 1.25
            self._zoom += 1
            if self._zoom > 0:
                self.scale(self.factor, self.factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0
    
    def on_zoom_out(self):
        if self.hasPhoto():
            self.factor = 0.8
            self._zoom -= 1
            if self._zoom > 0:
                self.scale(self.factor, self.factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
           

    def onClicked(self):
        self.flag = True
        self.update()
        

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
        super(leftImagePhotoViewer, self).mousePressEvent(event)

    def get_line(self):
        xi = int(self.x1)
        xf = int(self.x2)
        yi = int(self.y1)
        yf = int(self.y2)
        #self.pix=self._photo.pixmap().toImage().pixel(xf,yf)
        #print(QColor(self.pix).getRgbF())
        print("new")
        y = abs(self.y1-self.y2)
        x = abs(self.x1-self.x2)
        print("y:",y)
        if y>3:
            print("1")
            if x>3:
                slope = (self.y2-self.y1)/(self.x2-self.x1)
                c = self.y1-self.x1*slope
                if xi > xf:
                    xf = int(self.x1)
                    xi = int(self.x2)
                    yf = int(self.y1)
                    yi = int(self.y2)
                    
                while xi <= xf:
                    y = int(slope* xi + c)
                    #print("-------")
                    self.pix=self._photo.pixmap().toImage().pixel(xi,y)
                    #print(QColor(self.pix).getRgbF())
                    if QColor(self.pix).getRgbF() >= (0.1,0.1,0.1,1.0):
                        self._scene.addEllipse(xi,y , 1, 0, QPen(Qt.red), QBrush(Qt.red))
                        self.points.append((xi, y))
                    xi += 1
            else:
                xx =xi#int((yi+yf)/2)
                if yi <= yf:
                    while yi <= yf:
                        self.pix=self._photo.pixmap().toImage().pixel(xi,yi)
                        #print(QColor(self.pix).getRgbF())
                        if QColor(self.pix).getRgbF() >= (0.1,0.1,0.1,1.0):
                            self._scene.addEllipse(xx,yi , 1, 0, QPen(Qt.red), QBrush(Qt.green))
                            self.points.append((xx, yi))
                        yi +=1
                else:
                    while yi >= yf:    
                        self.pix=self._photo.pixmap().toImage().pixel(xi,yi)
                        #print(QColor(self.pix).getRgbF())
                        if QColor(self.pix).getRgbF() >= (0.1,0.1,0.1,1.0):
                            self._scene.addEllipse(xx,yi , 1, 0, QPen(Qt.red), QBrush(Qt.green))
                            self.points.append((xx, yi))
                        yi -=1
        else:
            print("2")
            #yy =int((yi+yf)/2)
            
            if xi <= xf:
                while xi <= xf:
                    self.pix=self._photo.pixmap().toImage().pixel(xi,yi)
                    #print(QColor(self.pix).getRgbF())
                    if QColor(self.pix).getRgbF() >= (0.1,0.1,0.1,1.0):
                        self._scene.addEllipse(xi,yi , 1, 0, QPen(Qt.red), QBrush(Qt.green))
                        self.points.append((xi, yi))
                    xi +=1
            else:
                while xi >= xf:    
                    self.pix=self._photo.pixmap().toImage().pixel(xi,yi)
                    #print(QColor(self.pix).getRgbF())
                    if QColor(self.pix).getRgbF() >= (0.1,0.1,0.1,1.0):
                        self._scene.addEllipse(xi,yi , 1, 0, QPen(Qt.red), QBrush(Qt.green))
                        self.points.append((xi, yi))
                    xi -=1
                        
        self.getNewOuterPoint()
        #print(slope)
        #print(points)
        #return points
        
    def getNewOuterPoint(self):
        self.points.sort(key=sortFirst)
        length = len(self.points)
        print(self.points)
        #print(self.points[0])
        #print(self.points[length-1])
        if Enquiry(self.points):
            self.x1, self.y1 = self.points[0]
            self.x2, self.y2 = self.points[length-1]
            self.distance = (((self.x1-self.x2)**2+(self.y1-self.y2)**2)**(1/2))*(10/604.119412)
        else:
            self.distance = 0
        #self.points.sort(key=sortSecond)
        #print(self.points)
        
        
def Enquiry(points):
    if len(points)== 0:
        return 0
    else:
        return 1
         

def sortFirst(val):
    return val[0]

def sortSecond(val):
    return val[1]
