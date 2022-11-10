# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v6_test_photo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage # 展示图片
#from dumbDialog import DumbDialog  
from PyQt5.QtWidgets import *

class Ui_photo_show(QWidget):
    def setupUi(self, photo_show):
        photo_show.setObjectName("photo_show")
        photo_show.resize(738, 678)
        self.label = QtWidgets.QLabel(photo_show)
        self.label.setGeometry(QtCore.QRect(140, 90, 471, 471))
        self.label.setObjectName("label")

        pix = QPixmap('1.png')

        # lb1 = QLabel(self)
        # lb1.setGeometry(0,0,500,210)
        # lb1.setStyleSheet("border: 2px solid red")
        # lb1.setPixmap(pix)

        # lb2 = QLabel(self)
        # lb2.setGeometry(0,250,500,410)
        self.label.setPixmap(pix)

        self.retranslateUi(photo_show)
        QtCore.QMetaObject.connectSlotsByName(photo_show)

    def retranslateUi(self, photo_show):
        _translate = QtCore.QCoreApplication.translate
        photo_show.setWindowTitle(_translate("photo_show", "Form"))
        self.label.setText(_translate("photo_show", "TextLabel"))

    def add_child_function(self):
        #print('child row is {}, col is {}'.format(self._row, self._col))
        print('ok')
    
    def show_photo(self, row, col):
        print('child row is {}, col is {}'.format(row, col))
        # self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".", 
        #     "Image Files(*.jpg *.jpeg *.png)")[0]
        self.filename = '1.png'
        # if len(self.filename):
        #     self.image = QImage(self.filename)
        #     self.imageView.setPixmap(QPixmap.fromImage(self.image))
        #     self.resize(self.image.width(), self.image.height())
        pix = QPixmap('1.png')

        # lb1 = QLabel(self)
        # lb1.setGeometry(0,0,500,210)
        # lb1.setStyleSheet("border: 2px solid red")
        # lb1.setPixmap(pix)

        # lb2 = QLabel(self)
        # lb2.setGeometry(0,250,500,410)
        self.label.setPixmap(pix)
        self.show()