# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v6_test_photo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_photo_show(object):
    def setupUi(self, photo_show):
        photo_show.setObjectName("photo_show")
        photo_show.resize(738, 678)
        self.label = QtWidgets.QLabel(photo_show)
        self.label.setGeometry(QtCore.QRect(140, 90, 471, 471))
        self.label.setObjectName("label")

        self.retranslateUi(photo_show)
        QtCore.QMetaObject.connectSlotsByName(photo_show)

    def retranslateUi(self, photo_show):
        _translate = QtCore.QCoreApplication.translate
        photo_show.setWindowTitle(_translate("photo_show", "Form"))
        self.label.setText(_translate("photo_show", "this is a lable"))

