# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(781, 763)
        self.widget_top = QtWidgets.QWidget(Form)
        self.widget_top.setGeometry(QtCore.QRect(0, 0, 781, 31))
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
        self.v_line = QtWidgets.QFrame(Form)
        self.v_line.setGeometry(QtCore.QRect(80, 30, 20, 701))
        self.v_line.setStyleSheet("Qline#v_line{background:rgb(0, 170, 255)}\n"
"color: rgb(0, 170, 255);")
        self.v_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line.setObjectName("v_line")
        self.main_pushButton_2 = QtWidgets.QPushButton(Form)
        self.main_pushButton_2.setGeometry(QtCore.QRect(0, 310, 89, 17))
        self.main_pushButton_2.setObjectName("main_pushButton_2")
        self.main_pushButton_0 = QtWidgets.QPushButton(Form)
        self.main_pushButton_0.setGeometry(QtCore.QRect(0, 250, 89, 17))
        self.main_pushButton_0.setObjectName("main_pushButton_0")
        self.main_pushButton_1 = QtWidgets.QPushButton(Form)
        self.main_pushButton_1.setGeometry(QtCore.QRect(0, 280, 89, 17))
        self.main_pushButton_1.setObjectName("main_pushButton_1")
        self.main_pushButton_3 = QtWidgets.QPushButton(Form)
        self.main_pushButton_3.setGeometry(QtCore.QRect(0, 340, 89, 16))
        self.main_pushButton_3.setObjectName("main_pushButton_3")
        self.main_stackedWidget = QtWidgets.QStackedWidget(Form)
        self.main_stackedWidget.setGeometry(QtCore.QRect(150, 90, 521, 611))
        self.main_stackedWidget.setAcceptDrops(True)
        self.main_stackedWidget.setAutoFillBackground(False)
        self.main_stackedWidget.setObjectName("main_stackedWidget")
        self.main_page_0 = QtWidgets.QWidget()
        self.main_page_0.setObjectName("main_page_0")
        self.label_5 = QtWidgets.QLabel(self.main_page_0)
        self.label_5.setGeometry(QtCore.QRect(70, 20, 144, 16))
        self.label_5.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.label_5.setObjectName("label_5")
        self.main_stackedWidget.addWidget(self.main_page_0)
        self.main_page_1 = QtWidgets.QWidget()
        self.main_page_1.setObjectName("main_page_1")
        self.label_10 = QtWidgets.QLabel(self.main_page_1)
        self.label_10.setGeometry(QtCore.QRect(11, 198, 45, 16))
        self.label_10.setObjectName("label_10")
        self.radioButton_2 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_2.setGeometry(QtCore.QRect(74, 164, 68, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_7 = QtWidgets.QLabel(self.main_page_1)
        self.label_7.setGeometry(QtCore.QRect(11, 181, 45, 16))
        self.label_7.setObjectName("label_7")
        self.radioButton = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton.setGeometry(QtCore.QRect(74, 181, 68, 16))
        self.radioButton.setObjectName("radioButton")
        self.label_9 = QtWidgets.QLabel(self.main_page_1)
        self.label_9.setGeometry(QtCore.QRect(11, 164, 32, 16))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.main_page_1)
        self.label_8.setGeometry(QtCore.QRect(11, 148, 284, 16))
        self.label_8.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.main_page_1)
        self.label_11.setGeometry(QtCore.QRect(11, 219, 59, 16))
        self.label_11.setObjectName("label_11")
        self.radioButton_3 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_3.setGeometry(QtCore.QRect(74, 198, 68, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_4.setGeometry(QtCore.QRect(74, 219, 68, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_5.setGeometry(QtCore.QRect(74, 256, 68, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_12 = QtWidgets.QLabel(self.main_page_1)
        self.label_12.setGeometry(QtCore.QRect(11, 240, 293, 16))
        self.label_12.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.main_page_1)
        self.label_14.setGeometry(QtCore.QRect(11, 273, 45, 16))
        self.label_14.setObjectName("label_14")
        self.radioButton_6 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_6.setGeometry(QtCore.QRect(74, 273, 68, 16))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_15 = QtWidgets.QLabel(self.main_page_1)
        self.label_15.setGeometry(QtCore.QRect(11, 290, 45, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.main_page_1)
        self.label_16.setGeometry(QtCore.QRect(11, 307, 59, 16))
        self.label_16.setObjectName("label_16")
        self.radioButton_7 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_7.setGeometry(QtCore.QRect(74, 290, 68, 16))
        self.radioButton_7.setObjectName("radioButton_7")
        self.label_19 = QtWidgets.QLabel(self.main_page_1)
        self.label_19.setGeometry(QtCore.QRect(11, 340, 32, 16))
        self.label_19.setObjectName("label_19")
        self.radioButton_8 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_8.setGeometry(QtCore.QRect(74, 307, 68, 16))
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_17 = QtWidgets.QLabel(self.main_page_1)
        self.label_17.setGeometry(QtCore.QRect(11, 324, 283, 16))
        self.label_17.setStyleSheet("font: 63 9pt \"Segoe UI Semibold\";")
        self.label_17.setObjectName("label_17")
        self.radioButton_11 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_11.setGeometry(QtCore.QRect(74, 340, 68, 16))
        self.radioButton_11.setObjectName("radioButton_11")
        self.label_20 = QtWidgets.QLabel(self.main_page_1)
        self.label_20.setGeometry(QtCore.QRect(11, 357, 45, 16))
        self.label_20.setObjectName("label_20")
        self.radioButton_10 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_10.setGeometry(QtCore.QRect(74, 357, 68, 16))
        self.radioButton_10.setObjectName("radioButton_10")
        self.label_18 = QtWidgets.QLabel(self.main_page_1)
        self.label_18.setGeometry(QtCore.QRect(11, 374, 45, 16))
        self.label_18.setObjectName("label_18")
        self.radioButton_9 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_9.setGeometry(QtCore.QRect(74, 374, 68, 16))
        self.radioButton_9.setObjectName("radioButton_9")
        self.label_23 = QtWidgets.QLabel(self.main_page_1)
        self.label_23.setGeometry(QtCore.QRect(11, 391, 59, 16))
        self.label_23.setObjectName("label_23")
        self.radioButton_12 = QtWidgets.QRadioButton(self.main_page_1)
        self.radioButton_12.setGeometry(QtCore.QRect(74, 391, 68, 16))
        self.radioButton_12.setObjectName("radioButton_12")
        self.label_13 = QtWidgets.QLabel(self.main_page_1)
        self.label_13.setGeometry(QtCore.QRect(11, 256, 32, 16))
        self.label_13.setObjectName("label_13")
        self.main_stackedWidget.addWidget(self.main_page_1)
        self.main_page_2 = QtWidgets.QWidget()
        self.main_page_2.setObjectName("main_page_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_page_2)
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.main_page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 60, 71, 19))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.splitter_3 = QtWidgets.QSplitter(self.main_page_2)
        self.splitter_3.setGeometry(QtCore.QRect(181, 98, 155, 19))
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
        self.splitter_4 = QtWidgets.QSplitter(self.main_page_2)
        self.splitter_4.setGeometry(QtCore.QRect(181, 137, 155, 19))
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
        self.splitter_5 = QtWidgets.QSplitter(self.main_page_2)
        self.splitter_5.setGeometry(QtCore.QRect(181, 175, 155, 19))
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
        self.label = QtWidgets.QLabel(self.main_page_2)
        self.label.setGeometry(QtCore.QRect(181, 21, 90, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.main_page_2)
        self.lineEdit.setGeometry(QtCore.QRect(270, 20, 71, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.main_page_2)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 50, 16))
        self.label_2.setObjectName("label_2")
        self.main_stackedWidget.addWidget(self.main_page_2)
        self.main_page_3 = QtWidgets.QWidget()
        self.main_page_3.setObjectName("main_page_3")
        self.listView = QtWidgets.QListView(self.main_page_3)
        self.listView.setGeometry(QtCore.QRect(80, 50, 421, 371))
        self.listView.setObjectName("listView")
        self.main_stackedWidget.addWidget(self.main_page_3)
        self.widget_top_2 = QtWidgets.QWidget(Form)
        self.widget_top_2.setGeometry(QtCore.QRect(0, 730, 781, 31))
        self.widget_top_2.setStyleSheet("QWidget#widget_top{background:rgb(0, 170, 255)}\n"
"color: rgb(0, 170, 255);")
        self.widget_top_2.setObjectName("widget_top_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.widget_top_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.retranslateUi(Form)
        self.main_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.v_line.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.main_pushButton_2.setText(_translate("Form", "????????????"))
        self.main_pushButton_0.setText(_translate("Form", "????????????"))
        self.main_pushButton_1.setText(_translate("Form", "????????????"))
        self.main_pushButton_3.setText(_translate("Form", "??????"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; font-style:italic; color:#55aaff;\">Welcome to CBR programme</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "Insulation"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.label_7.setText(_translate("Form", "Complexity"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.label_9.setText(_translate("Form", "U value"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p>Which of the following attributes do you think is the most important?</p></body></html>"))
        self.label_11.setText(_translate("Form", "Coagulability"))
        self.radioButton_3.setText(_translate("Form", "RadioButton"))
        self.radioButton_4.setText(_translate("Form", "RadioButton"))
        self.radioButton_5.setText(_translate("Form", "RadioButton"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p>Which of the following attributes do you think is the second important?</p></body></html>"))
        self.label_14.setText(_translate("Form", "Complexity"))
        self.radioButton_6.setText(_translate("Form", "RadioButton"))
        self.label_15.setText(_translate("Form", "Insulation"))
        self.label_16.setText(_translate("Form", "Coagulability"))
        self.radioButton_7.setText(_translate("Form", "RadioButton"))
        self.label_19.setText(_translate("Form", "U value"))
        self.radioButton_8.setText(_translate("Form", "RadioButton"))
        self.label_17.setText(_translate("Form", "<html><head/><body><p>Which of the following attributes do you think is the third important?</p></body></html>"))
        self.radioButton_11.setText(_translate("Form", "RadioButton"))
        self.label_20.setText(_translate("Form", "Complexity"))
        self.radioButton_10.setText(_translate("Form", "RadioButton"))
        self.label_18.setText(_translate("Form", "Insulation"))
        self.radioButton_9.setText(_translate("Form", "RadioButton"))
        self.label_23.setText(_translate("Form", "Coagulability"))
        self.radioButton_12.setText(_translate("Form", "RadioButton"))
        self.label_13.setText(_translate("Form", "U value"))
        self.pushButton_6.setText(_translate("Form", "execute"))
        self.pushButton_5.setText(_translate("Form", "add"))
        self.label_24.setText(_translate("Form", "Complexity          "))
        self.comboBox_2.setItemText(0, _translate("Form", "very low"))
        self.comboBox_2.setItemText(1, _translate("Form", "low"))
        self.comboBox_2.setItemText(2, _translate("Form", "medium"))
        self.comboBox_2.setItemText(3, _translate("Form", "high"))
        self.comboBox_2.setItemText(4, _translate("Form", "very high"))
        self.label_21.setText(_translate("Form", "Insulation          "))
        self.comboBox_1.setItemText(0, _translate("Form", "very low"))
        self.comboBox_1.setItemText(1, _translate("Form", "low"))
        self.comboBox_1.setItemText(2, _translate("Form", "medium"))
        self.comboBox_1.setItemText(3, _translate("Form", "high"))
        self.comboBox_1.setItemText(4, _translate("Form", "very high"))
        self.label_22.setText(_translate("Form", "Coagulability       "))
        self.comboBox_3.setItemText(0, _translate("Form", "very low"))
        self.comboBox_3.setItemText(1, _translate("Form", "low"))
        self.comboBox_3.setItemText(2, _translate("Form", "medium"))
        self.comboBox_3.setItemText(3, _translate("Form", "high"))
        self.comboBox_3.setItemText(4, _translate("Form", "very high"))
        self.label.setText(_translate("Form", "Case Name           "))
        self.label_2.setText(_translate("Form", "U value    "))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_Form()  #  ui_from?????????
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())