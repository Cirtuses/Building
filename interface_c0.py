from v6 import *
# from parent import *
from v6_child import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        # self.main_ui.__init__()
        self.main_ui.setupUi(self)
        self.main_ui.retranslateUi(self)


class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        # self.child = Ui_photo_show()
        # self.child.setupUi(self)
        # self.child.retranslateUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    child = childWindow()

    # 通过toolButton将两个窗体关联
    # btn=window.main_ui.toolButton
    # btn.clicked.connect(child.show)
    # window.main_ui.tableWidget.cellClicked['int','int'].connect(self.child_show)
    click_table_1 = window.main_ui.tableWidget
    click_table_1.cellClicked['int', 'int'].connect(child.child.show_photo)
    # 显示
    window.show()
    sys.exit(app.exec_())
