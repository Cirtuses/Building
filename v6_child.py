# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v6_child.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage # 展示图片
#from dumbDialog import DumbDialog  
from PyQt5.QtWidgets import *


import os
import os.path
from PIL import Image
import pandas as pd
import numpy as np

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self,  parent = None): 
        super().__init__()
        self._title = "show_case" #设置类实例成员_title,它的值为字符串的"image_laoder"
        self._diawidth = 500 #设置实例成员_diawidth,它的值为300
        self._diaheight = 450 
        self.setWindowTitle(self._title) #设置窗口标题
        self.setMinimumHeight(self._diaheight) #设置窗口最小的大小
        self.setMinimumWidth(self._diawidth)
        self.imageView = QLabel("add a image file") #得到一个QLabel的实例，并将它保存在成员imageView里，负责显示消息以及图片
        self.imageView.setAlignment(Qt.AlignCenter) #设置QLabel居中显示
        # self.btn_open = QPushButton("open") #实例化一个名为"open"的按钮，并将它保存在类成员btn_open中，负责去得到图片的路径，并在QLabel中显示
        # self.btn_open.clicked.connect(self.on_btn_open_clicked) #pyqt5中信号与槽的连接
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.imageView)
        # self.vlayout.addWidget(self.btn_open)
        self.setLayout(self.vlayout)

    def add_child_function(self):
        #print('child row is {}, col is {}'.format(self._row, self._col))
        print('ok')
    
    def show_test(self):
        pix = QPixmap('1.png')
        print('1')
        self.label.setPixmap(pix)
    
    def on_btn_open_clicked(self, checked):
        self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".","Image Files(*.jpg *.jpeg *.png)")[0]
        #self.filename = '1.png'
        print(self.filename)
        if len(self.filename):
            self.image = QImage(self.filename)
            self.imageView.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())

    def show_photo(self, row, col):
        path_openfile_name = 'Case-to-Case_v2_Result.xlsx'
        if len(path_openfile_name) > 0:
            input_table = pd.read_excel(path_openfile_name)
        input_table_colunms = input_table.shape[1]

        input_table_header = input_table.columns.values.tolist()
        input_table_header[0] = 'case name'
        input_table.columns = input_table_header
        print(input_table.loc[row][0])
        filename = str(input_table.loc[row][0]) + '.png'
        self.filename = adjust_photo(photo_in = filename)

        print(self.filename)
        if len(self.filename):
            self.image = QImage(self.filename)
            self.imageView.setPixmap(QPixmap.fromImage(self.image))
            self.resize(self.image.width(), self.image.height())
        self.show()


    def adjust_photo(photo_in, photo_out, width, height, type):
        img = Image.open(photo_in)
        out = img.resize((width, height),Image.ANTIALIAS)
        #resize image with high-quality
        out.save(photo_out, type)
        return out


if __name__== '__main__':
    app = QApplication([]);  # argv)
    win = Ui_Dialog()
    win.show()
    sys.exit(app.exec_())