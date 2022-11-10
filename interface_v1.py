# -*- coding:UTF-8 -*-
import sys
import os
import csv
import execute
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
#from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, QVBoxLayout, QLineEdit, QAction, QTextEdit, QLabel, QApplication
from PyQt5.QtWidgets import *
csv_filename = "datebase.csv"

num_of_category_a = 4
num_of_category_b = 2
category_num = 6
mylist = []


class CBR_interface(QWidget):
    def __init__(self, _cb=[], _test_item=[]):
        super().__init__()
        self.cb = _cb  # check box
        self.initUI()

    def initUI(self):
        line = []
        lb = []
        print("use this initUI")
        #        print(sys.argv[1])

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('CBR interface')
        
        self.tx = QTextEdit(self)
        self.tx.setGeometry(100, 500, 800, 200)
        self.tx.setStyleSheet('background-color:white; font:20px')
        #self.tx.setHorizontalScrollBarPolicy(2)
        self.tx.verticalScrollBarPolicy()
        self.tx.setLineWrapMode(1)
        
        

        h = 50
        # for i in range(category_num):
        #     line.append(QLineEdit(self))
        #     # line[i].setTextMargins(10,20,30,40)
        #     line[i].move(500, h * (i + 1))

        # for i in range(category_num):
        #     lb.append(QLabel(),self)
        
        ln1 = QLineEdit(self)
        ln1.move(500, h*1)

        select_bt1 = QPushButton("medium",self)
        select_bt2 = QPushButton("medium",self)
        select_bt3 = QPushButton("medium",self)
        select_bt1.move(500, h*2)
        select_bt2.move(500, h*3)
        select_bt3.move(500, h*4)
        select_bt1.setStyleSheet('background-color:white; font:20px')

        menu = QMenu(self)
        menu.addAction('very low')
        menu.addSeparator()
        menu.addAction('low')
        menu.addSeparator()
        menu.addAction('high')
        menu.addSeparator()
        menu.addAction('very high')

        select_bt1.setMenu(menu)
        select_bt2.setMenu(menu)
        select_bt3.setMenu(menu)

        lb1 = QLabel('U value', self)
        lb2 = QLabel('comlexity', self)
        lb3 = QLabel('insulation capacity', self)
        lb4 = QLabel('possibility for condenstation', self)
        lb5 = QLabel('HVAC能耗效率', self)
        lb6 = QLabel('照明能耗效率', self)
        
        lb_start_pos = 250

        lb1.move(lb_start_pos, h*1)
        lb2.move(lb_start_pos, h*2)
        lb3.move(lb_start_pos, h*3)
        lb4.move(lb_start_pos, h*4)
        lb5.move(lb_start_pos, h*5)
        lb6.move(lb_start_pos, h*6)

        # line1 = QLineEdit(self)
        # line1.move(100,200)
        # action = QAction(self)
        # action.setIcon(QIcon('check.ico'))
        # action.triggered.connect(lambda:self.check(line1))
        # line1.addAction(action,QLineEdit.TrailingPosition)
         
        bt1 = QPushButton('confirm', self)
        bt2 = QPushButton('add', self)
        bt3 = QPushButton('cancel', self)
        bt4 = QPushButton('exit', self)

        bt1.clicked.connect(lambda: self.confirm(line))
        bt2.clicked.connect(lambda: self.add_case(line))
        # bt3.clicked.connect(self.showDialog)
        bt4.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(bt1, 1)
        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(bt2)
        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(bt3)
        hbox.addStretch(1)  # 增加伸缩量
        hbox.addWidget(bt4)
        hbox.addStretch(1)

        
        # 垂直布局的默认摆放是从上往下,这里添加一个伸缩量占满上方的剩余空间，那么上面两个按键所在的布局就会往下跑
        vbox.addStretch(1)
        # 把水平布局添加到垂直布局
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # bt1.setGeometry(780, 800, 100, 100)  # 相对于界面左上角的位置

        # for i in range(len(self.test_item)):
        #     if i == 0:
        #         self.cb[0].stateChanged.connect(self.changecb1())
        #     else:
        #         self.cb[i].stateChanged.connect(self.changecb2())

        #        bt1.clicked.connect(self.confirm)

        # bt1.connect(self.execute())

        self.show()
        print("has show")
    


    def confirm(self, line):
        mylist = []
        for i in range(category_num):
            myline = line[i].text()
            mylist.append(myline)
        print(mylist)
        input_a = list(map(int, mylist[:4]))
        input_b = list(map(int, mylist[4:]))
        print(input_a, input_b)
        self.logger.info('The progress is starting')
        execute.execute_programme(input_a, input_b)
        return mylist

    def add_case(self, line):
        mylist = []
        for i in range(category_num):
            myline = line[i].text()
            mylist.append(myline)
        mylist = list(map(int, mylist))
        self.logger_info('new case is {}'.format(mylist))
        execute.add_to_database('database.xlsx', 0, mylist)
        QMessageBox.about(self, 'Message', 'Successfully add new case to database')
        self.logger_info('Successfully add new case to database')

    def check(self, line):
        myline = line.text()
        print(myline)
        QMessageBox.information(self, '提示信息', '你或许想要表达的单词是' + myline)

    def showDialog(self):
        #num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")  
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0,num) 
        for i in range(num):
            progress.setValue(i) 
            if progress.wasCanceled():
                QMessageBox.warning(self,"提示","操作失败") 
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self,"提示","操作成功")
    
    def logger_info(self, log):
        self.tx.append(log)


    def changecb1(self):
        if self.cb[0].checkState() == Qt.Checked:
            for i in range(len(self.test_item)):
                if i == 0:
                    pass
                else:
                    self.cb[i].setChecked(True)
        elif self.cb[0].checkState() == Qt.Unchecked:
            for i in range(len(self.test_item)):
                if i == 0:
                    pass
                else:
                    self.cb[i].setChecked(False)

    def changecb2(self):
        pass
    
    def read_message(self, line):
        pass



    def execute(self):
        pass

    def set_tile(self, title=''):
        self.setWindowTitle(title)

    # error
    # def event(self):
    #     pass

    def add_notes(self, file="tiger_fatp_eol1.yaml"):
        bflag = False
        with open(file, encoding='utf-8') as f, open('temp.yaml', 'w', encoding='utf-8') as new_f:
            for line in f:
                new_line = '#' + line
                new_f.write(new_line)
            os.remove(file)
            os.rename('temp.yaml', file)
            bflag = True
        if bflag:
            QMessageBox.about(self, 'Message', 'Successfully modified')

    def delete_notes(self, file="tiger_fatp_eol1.yaml"):
        bflag = False
        with open(file, encoding='utf-8') as f, open('temp.yaml', 'w', encoding='utf-8') as new_f:
            for line in f:
                new_line = line.split('#')[0]
                new_f.write(new_line)
            os.remove(file)
            os.rename('temp.yaml', file)
        if bflag:
            QMessageBox.about(self, 'Message', 'Successfully modified')


'''
两个函数：
勾选则加注释
不勾选或者取消勾选 则注释取消
box 文本处理
'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    yaml_interface = CBR_interface()
    exit(app.exec_())
