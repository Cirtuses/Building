# -*- coding:UTF-8 -*-
import sys
import os
import csv
import time
import execute
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
#from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, QVBoxLayout, QLineEdit, QAction, QTextEdit, QLabel, QApplication
from PyQt5.QtWidgets import *
xlsx_filename = "database_v1.xlsx"

num_of_category_a = 4
num_of_category_b = 2
category_num = 6
mylist = []


class CBR_interface(QWidget):
    def __init__(self, _cb=[], _test_item=[]):
        super().__init__()
        self.setGeometry(300, 300, 1000, 1000)
        self.setFixedSize(self.width(), self.height())  #设置固定大小


		self.stack1= QWidget()
		self.stack2= QWidget()
		self.stack3= QWidget()

		self.stack1UI()
		self.stack2UI()
		self.stack3UI()
#        self.stack4UI()
        


		self.Stack = QStackedWidget (self)
		self.Stack.addWidget (self.stack1)
		self.Stack.addWidget (self.stack2)
		self.Stack.addWidget (self.stack3)

		hbox = QHBoxLayout(self)
		hbox.addWidget(self.leftlist)
		hbox.addWidget(self.Stack)
		self.setLayout(hbox)
        self.setWindowTitle("CBR interface")

    def tab4UI(self):
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 430, 211, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(180, 20, 261, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_24 = QtWidgets.QLabel(self.splitter_3)
        self.label_24.setObjectName("label_24")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_21 = QtWidgets.QLabel(self.splitter_4)
        self.label_21.setObjectName("label_21")
        self.comboBox_1 = QtWidgets.QComboBox(self.splitter_4)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_22 = QtWidgets.QLabel(self.splitter_5)
        self.label_22.setObjectName("label_22")
        self.comboBox_3 = QtWidgets.QComboBox(self.splitter_5)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.splitter_5)
        self.stackedWidget.addWidget(self.page_2)

    def stack1UI(self):
        self.case = {'name':'test', 'U value': 1, 'comlexity':'very low', 'insulation capacity':'very low', 'possibility for condenstation':'very low'}
        self.line = []
        lb = []
        print("use this initUI")
        #        print(sys.argv[1])

        # self.setGeometry(300, 300, 1000, 1000)
        # self.setWindowTitle('CBR interface')
        self.tx = QTextEdit(self)
        self.tx.setGeometry(100, 500, 800, 200)
        
        self.tx.setStyleSheet('background-color:white; font:20px')
        #self.tx.setHorizontalScrollBarPolicy(2)
        self.tx.verticalScrollBarPolicy()
        self.tx.setLineWrapMode(1)
        

        h = 70
        # for i in range(category_num):
        #     line.append(QLineEdit(self))
        #     # line[i].setTextMargins(10,20,30,40)
        #     line[i].move(500, h * (i + 1))

        # for i in range(category_num):
        #     lb.append(QLabel(),self)
        self.ln0 = QLineEdit(self)
        self.ln0.move(500, 20)

        self.ln1 = QLineEdit(self)
        self.ln1.move(500, h*1)

        # self.cb = QComboBox(self)
        # self.cb.move(100, 20)

        # # 单个添加条目
        # self.cb.addItem('C')
        # self.cb.addItem('C++')
        # self.cb.addItem('Python')
        # # 多个添加条目
        # self.cb.addItems(['Java', 'C#', 'PHP'])

        # # 信号
        # self.cb.currentIndexChanged[str].connect(self.print_value) # 条目发生改变，发射信号，传递条目内容
        # self.cb.currentIndexChanged[int].connect(self.print_value)  # 条目发生改变，发射信号，传递条目索引
        # self.cb.highlighted[str].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目内容
        # self.cb.highlighted[int].connect(self.print_value)  # 在下拉列表中，鼠标移动到某个条目时发出信号，传递条目索引
    
        select_bt1 = QComboBox(self)
        select_bt2 = QComboBox(self)
        select_bt3 = QComboBox(self)

        select_bt1.move(500, h*2)
        select_bt2.move(500, h*3)
        select_bt3.move(500, h*4)
        #select_bt1.setStyleSheet('background-color:white; font:20px')

        select_bt1.addItems(['very low', 'low', 'medium', 'high', 'very high'])
        select_bt2.addItems(['very low', 'low', 'medium', 'high', 'very high'])
        select_bt3.addItems(['very low', 'low', 'medium', 'high', 'very high'])
        
        select_bt1.currentIndexChanged[str].connect(self.add_case_value_1) # 条目发生改变，发射信号，传递条目内容
        select_bt2.currentIndexChanged[str].connect(self.add_case_value_2)
        select_bt3.currentIndexChanged[str].connect(self.add_case_value_3)

        
        lb0 = QLabel('case name', self)
        lb1 = QLabel('U value', self)
        lb2 = QLabel('comlexity', self)
        #lb3 = QLabel('insulation capacity', self)
        lb3 = QLabel('绝缘能力', self)
        
        lb4 = QLabel('凝结的可能性', self)
        #lb4 = QLabel('possibility for condenstation', self)
        
        lb_start_pos = 250
        

        lb0.move(lb_start_pos, 20)
        lb1.move(lb_start_pos, h*1)
        lb2.move(lb_start_pos, h*2)
        lb3.move(lb_start_pos, h*3)
        lb4.move(lb_start_pos, h*4)

        # line1 = QLineEdit(self)
        # line1.move(100,200)
        # action = QAction(self)
        # action.setIcon(QIcon('check.ico'))
        # action.triggered.connect(lambda:self.check(line1))
        # line1.addAction(action,QLineEdit.TrailingPosition)
         
        bt1 = QPushButton('execute', self)
        bt2 = QPushButton('add', self)
        bt3 = QPushButton('cancel', self)
        bt4 = QPushButton('exit', self)

        bt1.clicked.connect(lambda: self.confirm())
        bt2.clicked.connect(lambda: self.add_case())
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
        self.tab1.setLayout(vbox)

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
    
    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))    
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"),sex)
        layout.addRow("生日",QLineEdit())
        self.setTabText(1,"个人详细信息")
        self.tab2.setLayout(layout)
		
    def stack3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(2,"教育程度")
        self.tab3.setLayout(layout)

    def add_case_value_1(self, str):
        self.case['comlexity'] = str
        print(str)
    
    def add_case_value_2(self, str):
        self.case['insulation capacity'] = str
        print(str)
    
    def add_case_value_3(self, str):
        self.case['possibility for condenstation'] = str
        print(str)

    def confirm(self):
        tx1 = self.ln0.text() 
        tx2 = self.ln1.text() 
        if tx1 != '':
           self.case['name'] = tx1
        if tx2 != '':
           self.case['U value'] = tx2
        self.logger_info('target case is {}'.format(self.case))
        time.sleep(1)
        execute.execute_programme(self.case)
        self.logger_info("program execution completed")
        
        self.logger_info("the results is imported into Case-to-Case_vl_Result.xlsx")
        QMessageBox.about(self, 'Message', 'Successfully execute the program')

        #df = execute.read_database('Case-to-Case_vl_Result.xlsx', 0)
        #self.logger_info(df)
    
    def add_case(self):
        self.logger_info('adding case')
        tx1 = self.ln0.text() 
        tx2 = self.ln1.text() 
        if tx1 != '':
           self.case['name'] = tx1
        if tx2 != '':
           self.case['U value'] = tx2
        self.logger_info('new case is {}'.format(self.case))
        execute.add_to_database(xlsx_filename, 0, self.case)
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
