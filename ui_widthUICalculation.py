# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\anaconda3\envs\mythesisenv\benThesis\widthUICalculation.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 40, 1021, 571))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 29, 741, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.rightZoomInButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.rightZoomInButton.setObjectName("rightZoomInButton")
        self.horizontalLayout_5.addWidget(self.rightZoomInButton)
        self.rightZoomOutButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.rightZoomOutButton.setObjectName("rightZoomOutButton")
        self.horizontalLayout_5.addWidget(self.rightZoomOutButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_2.setStretch(1, 10)
        self.crackWidthTableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.crackWidthTableWidget.setGeometry(QtCore.QRect(780, 30, 221, 521))
        self.crackWidthTableWidget.setObjectName("crackWidthTableWidget")
        self.crackWidthTableWidget.setColumnCount(2)
        self.crackWidthTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.crackWidthTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.crackWidthTableWidget.setHorizontalHeaderItem(1, item)
        self.crackWidthTableWidget.verticalHeader().setMinimumSectionSize(23)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 520, 739, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.trackCrackWidthButton = QtWidgets.QPushButton(self.layoutWidget)
        self.trackCrackWidthButton.setObjectName("trackCrackWidthButton")
        self.horizontalLayout_6.addWidget(self.trackCrackWidthButton)
        self.calculateCrackWidthButton = QtWidgets.QPushButton(self.layoutWidget)
        self.calculateCrackWidthButton.setObjectName("calculateCrackWidthButton")
        self.horizontalLayout_6.addWidget(self.calculateCrackWidthButton)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.crackWidthLabel = QtWidgets.QLabel(self.layoutWidget)
        self.crackWidthLabel.setObjectName("crackWidthLabel")
        self.horizontalLayout_6.addWidget(self.crackWidthLabel)
        self.crackWidthLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.crackWidthLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.crackWidthLineEdit.setObjectName("crackWidthLineEdit")
        self.horizontalLayout_6.addWidget(self.crackWidthLineEdit)
        self.horizontalLayout_6.setStretch(2, 50)
        self.openFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFolderButton.setGeometry(QtCore.QRect(10, 0, 93, 31))
        self.openFolderButton.setObjectName("openFolderButton")
        self.detectCrackButton = QtWidgets.QPushButton(self.centralwidget)
        self.detectCrackButton.setGeometry(QtCore.QRect(700, 30, 93, 31))
        self.detectCrackButton.setObjectName("detectCrackButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Crack Length Annotation"))
        self.rightZoomInButton.setText(_translate("MainWindow", "Zoom In"))
        self.rightZoomOutButton.setText(_translate("MainWindow", "Zoom Out"))
        item = self.crackWidthTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Line"))
        item = self.crackWidthTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Crack Width (mm)"))
        self.trackCrackWidthButton.setText(_translate("MainWindow", "Trace Crack Width"))
        self.calculateCrackWidthButton.setText(_translate("MainWindow", "Calculate Crack Width"))
        self.crackWidthLabel.setText(_translate("MainWindow", "Crack Width (mm):"))
        self.crackWidthLineEdit.setText(_translate("MainWindow", "0.00"))
        self.openFolderButton.setText(_translate("MainWindow", "Open Image"))
        self.detectCrackButton.setText(_translate("MainWindow", "Detect Crack"))
