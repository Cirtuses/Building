# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import sys
import time
import sys
import os
import csv
import time
import execute
import pandas as pd
import numpy as np


from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

xlsx_filename = "database_v1.xlsx"


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_top = QtWidgets.QWidget(self.centralwidget)
        self.widget_top.setGeometry(QtCore.QRect(0, 0, 700, 20))
        self.widget_top.setStyleSheet("QWidget#widget_top{background:rgb(0, 170, 255)}\n"
"color: rgb(0, 170, 255);")
        self.widget_top.setObjectName("widget_top")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_top)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 30, 610, 520))
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")

        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.title_label = QtWidgets.QLabel(self.page_0)
        self.title_label.setGeometry(QtCore.QRect(70, 20, 144, 16))
        self.title_label.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.title_label.setObjectName("title_label")
        self.stackedWidget.addWidget(self.page_0)



        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.my_radioButton_3 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_3.setGeometry(QtCore.QRect(160, 130, 111, 21))
        self.my_radioButton_3.setObjectName("my_radioButton_3")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.my_radioButton_3, 3)
        self.label_4 = QtWidgets.QLabel(self.page_1)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 79, 16))
        self.label_4.setObjectName("label_4")

        self.sublime_pushButton_0 = QtWidgets.QPushButton(self.page_1)
        self.sublime_pushButton_0.setGeometry(QtCore.QRect(420, 450, 113, 32))
        self.sublime_pushButton_0.setObjectName("sublime_pushButton_0")

        self.my_radioButton_7 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_7.setGeometry(QtCore.QRect(160, 268, 100, 20))
        self.my_radioButton_7.setObjectName("my_radioButton_7")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.my_radioButton_7, 7)
        self.label_1 = QtWidgets.QLabel(self.page_1)
        self.label_1.setGeometry(QtCore.QRect(71, 73, 46, 16))
        self.label_1.setObjectName("label_1")
        self.question_label_0 = QtWidgets.QLabel(self.page_1)
        self.question_label_0.setGeometry(QtCore.QRect(71, 39, 511, 31))
        self.question_label_0.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.question_label_0.setObjectName("question_label_0")
        self.my_radioButton_0 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_0.setGeometry(QtCore.QRect(160, 70, 100, 20))
        self.my_radioButton_0.setObjectName("my_radioButton_0")
        self.buttonGroup.addButton(self.my_radioButton_0, 0)
        self.label_7 = QtWidgets.QLabel(self.page_1)
        self.label_7.setGeometry(QtCore.QRect(75, 246, 59, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.page_1)
        self.label_9.setGeometry(QtCore.QRect(71, 329, 46, 16))
        self.label_9.setObjectName("label_9")
        self.question_label_2 = QtWidgets.QLabel(self.page_1)
        self.question_label_2.setGeometry(QtCore.QRect(71, 310, 491, 16))
        self.question_label_2.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.question_label_2.setObjectName("question_label_2")
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 68, 16))
        self.label_2.setObjectName("label_2")
        self.my_radioButton_1 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_1.setGeometry(QtCore.QRect(160, 90, 100, 20))
        self.my_radioButton_1.setObjectName("my_radioButton_1")
        self.buttonGroup.addButton(self.my_radioButton_1, 1)
        self.question_label_1 = QtWidgets.QLabel(self.page_1)
        self.question_label_1.setGeometry(QtCore.QRect(75, 179, 501, 16))
        self.question_label_1.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.question_label_1.setObjectName("question_label_1")
        self.label_3 = QtWidgets.QLabel(self.page_1)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 59, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.page_1)
        self.label_6.setGeometry(QtCore.QRect(75, 222, 68, 16))
        self.label_6.setObjectName("label_6")
        self.my_radioButton_5 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_5.setGeometry(QtCore.QRect(160, 220, 100, 20))
        self.my_radioButton_5.setObjectName("my_radioButton_5")
        self.buttonGroup_2.addButton(self.my_radioButton_5, 5)
        self.my_radioButton_4 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_4.setGeometry(QtCore.QRect(160, 196, 100, 20))
        self.my_radioButton_4.setObjectName("my_radioButton_4")
        self.buttonGroup_2.addButton(self.my_radioButton_4, 4)
        self.my_radioButton_2 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_2.setGeometry(QtCore.QRect(160, 110, 100, 20))
        self.my_radioButton_2.setObjectName("my_radioButton_2")
        self.buttonGroup.addButton(self.my_radioButton_2, 2)
        self.label_8 = QtWidgets.QLabel(self.page_1)
        self.label_8.setGeometry(QtCore.QRect(75, 270, 79, 16))
        self.label_8.setObjectName("label_8")
        self.my_radioButton_6 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_6.setGeometry(QtCore.QRect(160, 244, 100, 20))
        self.my_radioButton_6.setObjectName("my_radioButton_6")
        self.buttonGroup_2.addButton(self.my_radioButton_6, 6)
        self.label_11 = QtWidgets.QLabel(self.page_1)
        self.label_11.setGeometry(QtCore.QRect(71, 377, 59, 16))
        self.label_11.setObjectName("label_11")
        self.my_radioButton_9 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_9.setGeometry(QtCore.QRect(156, 351, 100, 20))
        self.my_radioButton_9.setObjectName("my_radioButton_9")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.my_radioButton_9, 9)
        self.label_10 = QtWidgets.QLabel(self.page_1)
        self.label_10.setGeometry(QtCore.QRect(71, 353, 68, 16))
        self.label_10.setObjectName("label_10")
        self.my_radioButton_8 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_8.setGeometry(QtCore.QRect(156, 327, 100, 20))
        self.my_radioButton_8.setObjectName("my_radioButton_8")
        self.buttonGroup_3.addButton(self.my_radioButton_8, 8)
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(75, 198, 46, 16))
        self.label_5.setObjectName("label_5")
        self.my_radioButton_11 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_11.setGeometry(QtCore.QRect(156, 399, 100, 20))
        self.my_radioButton_11.setObjectName("my_radioButton_11")
        self.buttonGroup_3.addButton(self.my_radioButton_11, 11)
        self.label_12 = QtWidgets.QLabel(self.page_1)
        self.label_12.setGeometry(QtCore.QRect(71, 401, 79, 16))
        self.label_12.setObjectName("label_12")
        self.my_radioButton_10 = QtWidgets.QRadioButton(self.page_1)
        self.my_radioButton_10.setGeometry(QtCore.QRect(156, 375, 100, 20))
        self.my_radioButton_10.setObjectName("my_radioButton_10")
        self.buttonGroup_3.addButton(self.my_radioButton_10, 10)
        self.stackedWidget.addWidget(self.page_1)





        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 430, 211, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout.addWidget(self.pushButton_0)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 20, 261, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.input_label_0 = QtWidgets.QLabel(self.splitter)
        self.input_label_0.setObjectName("input_label_0")
        self.input_lineEdit_0 = QtWidgets.QLineEdit(self.splitter)
        self.input_lineEdit_0.setObjectName("input_lineEdit_0")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.input_label_1 = QtWidgets.QLabel(self.splitter_2)
        self.input_label_1.setObjectName("input_label_1")
        self.input_lineEdit_1 = QtWidgets.QLineEdit(self.splitter_2)
        self.input_lineEdit_1.setObjectName("input_lineEdit_1")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.input_label_2 = QtWidgets.QLabel(self.splitter_3)
        self.input_label_2.setObjectName("input_label_2")
        self.comboBox_0 = QtWidgets.QComboBox(self.splitter_3)
        self.comboBox_0.setObjectName("comboBox_0")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.comboBox_0.addItem("")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.input_label_3 = QtWidgets.QLabel(self.splitter_4)
        self.input_label_3.setObjectName("input_label_3")
        self.comboBox_1 = QtWidgets.QComboBox(self.splitter_4)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.input_label_4 = QtWidgets.QLabel(self.splitter_5)
        self.input_label_4.setObjectName("input_label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter_5)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.splitter_5)
        self.textEdit_0 = QtWidgets.QTextEdit(self.page_2)
        self.textEdit_0.setGeometry(QtCore.QRect(140, 260, 351, 111))
        self.textEdit_0.setObjectName("textEdit_0")
        self.stackedWidget.addWidget(self.page_2)



        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.show_pushButton = QtWidgets.QPushButton(self.page_3)
        self.show_pushButton.setGeometry(QtCore.QRect(450, 460, 113, 32))
        self.show_pushButton.setObjectName("show_pushButton")


        self.tableWidget = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget.setGeometry(QtCore.QRect(85, 51, 451, 361))

        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.stackedWidget.addWidget(self.page_3)
        self.listWidget_0 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_0.setGeometry(QtCore.QRect(0, 140, 81, 201))
        self.listWidget_0.setStyleSheet("")
        self.listWidget_0.setObjectName("listWidget_0")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_0.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_0.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_0.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_0.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_0.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.listWidget_0.currentRowChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_function()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#55aaff;\">Welcome to CBR programme</span></p></body></html>"))
        self.my_radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.label_4.setText(_translate("MainWindow", "Coagulability"))
        self.my_radioButton_7.setText(_translate("MainWindow", "RadioButton"))
        self.label_1.setText(_translate("MainWindow", "U value"))
        self.question_label_0.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Which of the following attributes do you think is the most important?</span></p></body></html>"))
        self.my_radioButton_0.setText(_translate("MainWindow", "RadioButton"))
        self.label_7.setText(_translate("MainWindow", "Insulation"))
        self.label_9.setText(_translate("MainWindow", "U value"))
        self.question_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Which of the following attributes do you think is the third important?</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Complexity"))
        self.my_radioButton_1.setText(_translate("MainWindow", "RadioButton"))
        self.question_label_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Which of the following attributes do you think is the second important?</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Insulation"))
        self.label_6.setText(_translate("MainWindow", "Complexity"))
        self.my_radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.my_radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.my_radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.label_8.setText(_translate("MainWindow", "Coagulability"))
        self.my_radioButton_6.setText(_translate("MainWindow", "RadioButton"))
        self.label_11.setText(_translate("MainWindow", "Insulation"))
        self.my_radioButton_9.setText(_translate("MainWindow", "RadioButton"))
        self.label_10.setText(_translate("MainWindow", "Complexity"))
        self.my_radioButton_8.setText(_translate("MainWindow", "RadioButton"))
        self.label_5.setText(_translate("MainWindow", "U value"))
        self.my_radioButton_11.setText(_translate("MainWindow", "RadioButton"))
        self.label_12.setText(_translate("MainWindow", "Coagulability"))
        self.my_radioButton_10.setText(_translate("MainWindow", "RadioButton"))
        self.pushButton_0.setText(_translate("MainWindow", "execute"))
        self.pushButton_1.setText(_translate("MainWindow", "add"))
        self.input_label_0.setText(_translate("MainWindow", "Case Name           "))
        self.input_label_1.setText(_translate("MainWindow", "U value             "))
        self.input_label_2.setText(_translate("MainWindow", "Complexity          "))
        self.comboBox_0.setItemText(0, _translate("MainWindow", "very low"))
        self.comboBox_0.setItemText(1, _translate("MainWindow", "low"))
        self.comboBox_0.setItemText(2, _translate("MainWindow", "medium"))
        self.comboBox_0.setItemText(3, _translate("MainWindow", "high"))
        self.comboBox_0.setItemText(4, _translate("MainWindow", "very high"))
        self.input_label_3.setText(_translate("MainWindow", "Insulation          "))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "very low"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "low"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "medium"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "high"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "very high"))
        self.input_label_4.setText(_translate("MainWindow", "Coagulability       "))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "very low"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "low"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "medium"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "high"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "very high"))
        __sortingEnabled = self.listWidget_0.isSortingEnabled()
        self.listWidget_0.setSortingEnabled(False)
        item = self.listWidget_0.item(0)
        item.setText(_translate("MainWindow", "界面"))
        item = self.listWidget_0.item(1)
        item.setText(_translate("MainWindow", "喜爱偏好"))
        item = self.listWidget_0.item(2)
        item.setText(_translate("MainWindow", "输入预期"))
        item = self.listWidget_0.item(3)
        item.setText(_translate("MainWindow", "结果推荐"))
        item = self.listWidget_0.item(4)
        item.setText(_translate("MainWindow", "其他"))
        self.listWidget_0.setSortingEnabled(__sortingEnabled)
    
    def add_function(self):
        self.case = {'name':'test', 'U value': 1, 'comlexity':'very low', 'insulation capacity':'very low', 'possibility for condenstation':'very low'}
        self.line = []
        self.importance = {'U value': 3, 'comlexity': 3, 'insulation capacity': 3, 'possibility for condenstation': 3}

        self.buttonGroup.buttonClicked.connect(self.choose_importance)
        self.buttonGroup_2.buttonClicked.connect(self.choose_importance)
        self.buttonGroup_3.buttonClicked.connect(self.choose_importance)
        self.sublime_pushButton_0.clicked.connect(self.submit_importance)
        
        self.comboBox_1.currentIndexChanged[str].connect(self.add_case_value_2)
        self.comboBox_2.currentIndexChanged[str].connect(self.add_case_value_1)
        self.comboBox_1.currentIndexChanged[str].connect(self.add_case_value_3)

        self.pushButton_0.clicked.connect(lambda: self.execute())
        self.pushButton_1.clicked.connect(lambda: self.add_case())
    
        self.show_pushButton.clicked.connect(self.show_table)
    
    def choose_importance(self):
        sender = self.sender()
        if sender == self.buttonGroup:
            if self.buttonGroup.checkedId() == 0:
                self.importance['U value'] = 0
            elif self.buttonGroup.checkedId() == 1:
                self.importance['comlexity'] = 0
            elif self.buttonGroup.checkedId() == 2:
                self.importance['insulation capacity'] = 0
            elif self.buttonGroup.checkedId() == 3:
                self.importance['possibility for condenstation'] = 0           
        elif sender == self.buttonGroup_2:
            if self.buttonGroup_2.checkedId() == 4:
                self.importance['U value'] = 1
            elif self.buttonGroup_2.checkedId() == 5:
                self.importance['comlexity'] = 1
            elif self.buttonGroup_2.checkedId() == 6:
                self.importance['insulation capacity'] = 1
            elif self.buttonGroup_2.checkedId() == 7:
                self.importance['possibility for condenstation'] = 1 
        elif sender == self.buttonGroup_3:
            if self.buttonGroup_3.checkedId() == 8:
                self.importance['U value'] = 2
            elif self.buttonGroup_3.checkedId() == 9:
                self.importance['comlexity'] = 2
            elif self.buttonGroup_3.checkedId() == 10:
                self.importance['insulation capacity'] = 2
            elif self.buttonGroup_3.checkedId() == 11:
                self.importance['possibility for condenstation'] = 2

    def submit_importance(self):
        bflag = True
        for key,value in self.importance.items():
            if value != 3:
                bflag = False
        print(self.importance)
        # if bflag == True:
            
        # else：
        

    def add_case_value_1(self, str):
        self.case['comlexity'] = str
        print(str)
    
    def add_case_value_2(self, str):
        self.case['insulation capacity'] = str
        print(str)
    
    def add_case_value_3(self, str):
        self.case['possibility for condenstation'] = str
        print(str)

    def execute(self):
        print("1")
        tx1 = self.input_lineEdit_0.text() 
        tx2 = self.input_lineEdit_1.text() 
        if tx1 != '':
           self.case['name'] = tx1
        if tx2 != '':
           self.case['U value'] = tx2
        self.logger_info('target case is {}'.format(self.case))
        time.sleep(1)
        execute.execute_programme(self.case, self.importance)
        self.logger_info("program execution completed")
        
        self.logger_info("the results is imported into Case-to-Case_vl_Result.xlsx")
        # QMessageBox.about(self, 'Message', 'Successfully execute the program')

        #df = execute.read_database('Case-to-Case_vl_Result.xlsx', 0)
        #self.logger_info(df)
    
    def add_case(self):
        self.logger_info('adding case')
        tx1 = self.input_lineEdit_0.text() 
        tx2 = self.input_lineEdit_1.text() 
        if tx1 != '':
           self.case['name'] = tx1
        if tx2 != '':
           self.case['U value'] = tx2
        self.logger_info('new case is {}'.format(self.case))
        execute.add_to_database(xlsx_filename, 0, self.case)
        # QMessageBox.about(self, 'Message', 'Successfully add new case to database')
        self.logger_info('Successfully add new case to database')
    
    def logger_info(self, log):
        self.textEdit_0.append(log)



    def show_table(self):
    ###===========读取表格，转换表格，===========================================
        path_openfile_name = 'Case-to-Case_v1_Result.xlsx'
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name)
        #print(input_table)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
        #print(input_table_rows)
        #print(input_table_colunms)
            input_table_header = input_table.columns.values.tolist()
        #print(input_table_header)

        ###===========读取表格，转换表格，============================================
        ###======================给tablewidget设置行列表头============================

            self.tableWidget.setColumnCount(input_table_colunms)
            self.tableWidget.setRowCount(input_table_rows)
            self.tableWidget.setHorizontalHeaderLabels(input_table_header)

        ###======================给tablewidget设置行列表头============================

        ###================遍历表格每个元素，同时添加到tablewidget中========================
            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                #print(input_table_rows_values)
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            #print(input_table_rows_values_list)
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                #print(input_table_items_list)
                # print(type(input_table_items_list))

        ###==============将遍历的元素添加到tablewidget中并显示=======================

                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items) 
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, newItem)  

        ###================遍历表格每个元素，同时添加到tablewidget中========================
        else:
            self.page_3.show()
            #self.centralWidget.show()



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()  #  ui_from是类名
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
