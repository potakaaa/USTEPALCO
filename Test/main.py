import sys, sqlite3, hashlib
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pages.login_page import Ui_MainWindow as LoginPage
from pages.dashboard import Ui_MainWindow as DashboardPage
#test
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__seed = "USTEPALCO"
        self.__db_file = 'USTEPALCO.db'
        self.__conn = sqlite3.connect(self.__db_file)
        self.__sql = self.__conn.cursor()
        self.__init_db()
        self.page_view('login')

    def __init_db(self):
        self.__sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, password TEXT NOT NULL)")
        self.__conn.commit()

    def __check_login(self):
        email = self.ui.edit_email.text()
        text_passw = self.ui.edit_password.text()
        hash_passw = self.secure_password(text_passw) 

        self.__sql.execute("SELECT * FROM users WHERE email = ? AND password = ?;",(email, hash_passw))
        results = self.__sql.fetchall()
        return True if len(results) > 0 else False
    
    def secure_password(self, plaintext):
        seed_text = self.__seed + plaintext
        ciphertext = hashlib.sha1(seed_text.encode())
        return ciphertext.hexdigest()
    
    def show_message(self, title, text, icon_type):
        msg = QMessageBox()
        msg.setIcon(icon_type)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setText(text)
        msg.exec_()

    def page_view(self, view):
        if view == 'login':
            self.ui = LoginPage()
        elif view == 'dashboard':
            self.ui = DashboardPage()

        self.ui.setupUi(self)

    def on_button_login_pressed(self):
        if self.__check_login():
            self.page_view('dashboard')
        else:
            self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
