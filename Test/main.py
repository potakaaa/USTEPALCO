import random
import sys, sqlite3, hashlib
from pages.mailer import Mail
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pages.login_page import Ui_MainWindow as LoginPage
from pages.dashboard2 import Ui_Dashboard_Window as DashboardPage

#test
class MainWindow(QMainWindow):
    def __init__(self):
        self.reset_password()  # remove this later
        exit()                  # remove this later
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

    def generate_otp(self):
        OTP_Length = 6
        OTP_Characters = list('ABCDEFGHJKLOPQRX132907')
        OTP_code = random.choices(OTP_Characters, k=OTP_Length)
        return ''.join(OTP_code)
    
    def reset_password(self):
        reset_code = self.generate_otp()
        user = "admin" # temp variable example  for later use
        subject = "Password reset on USTEPALCO"
        content = f"""
        <div>
        <table style="width:100%; height: 40vh; font-size:14px; background-color: rgb(0,0,0,0.1); display:flex; align-items:center; justify-content: center;">
            <tr>
            <td>
            <div style="min-width:350px; font-family: sans-serif; background-color: rgb(255,255,255,0.6); padding:10px; border-radius:10px; box-shadow:0px 0px 5px 1px rgb(0,0,0,0.2);">
                <h2 style="font-family: sans-serif; text-align: center;">RESET YOUR PASSWORD</h2>
                <p>
                    Hey {user},<br>
                    A password reset was requested for your account. Below is your authentication code:
                </p>
                <div style="text-align: center;">
                    <input readonly value="{reset_code}" style="border-radius:5px; padding:5px; font-family: sans-serif; text-align: center; color:black; font-size:28px; outline:none; border:1px solid black;">
                </div>
                <p>If you didn't request this change, please ignore this message or contact <a href="mailto:support@ustepalco.cloud">support</a> immediately.</p>
                <p>Kind Regards,<br><a style="text-decoration:underline;font-size:12px;text-align:center" href="https://ustepalco.cloud"><b>USTEPALCO</b></a></p>
            </div>
            </td>
            </tr>
        </table>
        </div>
        """
        mail = Mail(subject, content, "html")
        mail.sendto("abales.anikinluk3@gmail.com")

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
