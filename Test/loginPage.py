from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFrame, QApplication, QMessageBox
from PyQt5 import QtGui
import sys
from login_page import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #functions
    def on_button_login_pressed(self):
        error_msg = QMessageBox()
        error_msg.setIcon(QMessageBox.Warning)
        error_msg.setWindowTitle("ERROR")
        error_msg.setWindowIcon(QtGui.QIcon('icon.png'))
        error_msg.setText("Yapper!")
        x = error_msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())