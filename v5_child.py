# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v5_child.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_photo(QtWidgets.QWidget):
    def __init__(self):
        super(child_window,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, photo):
        photo.setObjectName("photo")
        photo.resize(742, 752)
        self.s_box = QtWidgets.QWidget(photo)
        self.s_box.setGeometry(QtCore.QRect(120, 80, 531, 581))
        self.s_box.setObjectName("s_box")
        self.retranslateUi(photo)
        QtCore.QMetaObject.connectSlotsByName(photo)

    def retranslateUi(self, photo):
        _translate = QtCore.QCoreApplication.translate
        photo.setWindowTitle(_translate("photo", "Form"))

