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
        super(MainWindow, self).__init__()
        self.__seed = "USTEPALCO"
        self.__db_file = self.__seed+'.db'
        self.__conn = sqlite3.connect(self.__db_file)
        self.__sql = self.__conn.cursor()
        self.__init_db()
        self.page_view('login')
        
    def __init_db(self):
        self.__sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, password TEXT NOT NULL)")
        self.__conn.commit()

    def __check_login(self, email, password):
        password = self.secure_password(password) 
        self.__sql.execute("SELECT * FROM users WHERE email = ? AND password = ?;",(email, password))
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

    def reset_password(self, email='abales.anikinluk3@gmail.com'):
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
        mail.sendto(email)

    def page_view(self, view):
        if view == 'login':
            self.ui = LoginPage()
        elif view == 'dashboard':
            self.ui = DashboardPage()

        self.ui.setupUi(self)

    def on_logout_button_pressed(self):
        response = QMessageBox.question(self, 'Logout', 'Are you sure you want to logout?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if response == QMessageBox.Yes:
            self.page_view('login')


    def on_button_login_pressed(self):
        '''email = self.ui.edit_email.text()
        passw = self.ui.edit_password.text()
        if((len(passw) < 8)):
            self.show_message("ERROR", "Minimum password length is 8.", QMessageBox.Warning)
        elif(self.__check_login(email, passw) ):
            self.page_view('dashboard')
        else:
            self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)'''
        
        self.page_view('dashboard')

    #change page
    def on_dashboard_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.dashboard_button.setStyleSheet("#dashboard_button {\n"
            "color: white; }\n"
        )
        self.ui.reports_button.setStyleSheet("#reports_button {\n"
            "color: #959595; }")
        self.ui.manage_button.setStyleSheet("#manage_button {\n"
            "color: #959595; }")
        self.ui.generate_button.setStyleSheet("#generate_button {\n"
            "color: #959595; }")
        self.ui.profile_button.setStyleSheet("#profile_button {\n"
            "color: #959595; }")
            
    def on_reports_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.reports_button.setStyleSheet("#reports_button {\n"
            "color: white; }\n"
        )
        self.ui.dashboard_button.setStyleSheet("#dashboard_button {\n"
            "color: #959595; }")
        self.ui.manage_button.setStyleSheet("#manage_button {\n"
            "color: #959595; }")
        self.ui.generate_button.setStyleSheet("#generate_button {\n"
            "color: #959595; }")
        self.ui.profile_button.setStyleSheet("#profile_button {\n"
            "color: #959595; }")
    def on_manage_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.manage_button.setStyleSheet("#manage_button {\n"
            "color: white; }\n"
        )
        self.ui.reports_button.setStyleSheet("#reports_button {\n"
            "color: #959595; }")
        self.ui.dashboard_button.setStyleSheet("#dashboard_button {\n"
            "color: #959595; }")
        self.ui.generate_button.setStyleSheet("#generate_button {\n"
            "color: #959595; }")
        self.ui.profile_button.setStyleSheet("#profile_button {\n"
            "color: #959595; }")
    def on_generate_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.generate_button.setStyleSheet("#generate_button {\n"
            "color: white; }\n"
        )
        self.ui.reports_button.setStyleSheet("#reports_button {\n"
            "color: #959595; }")
        self.ui.manage_button.setStyleSheet("#manage_button {\n"
            "color: #959595; }")
        self.ui.dashboard_button.setStyleSheet("#dashboard_button {\n"
            "color: #959595; }")
        self.ui.profile_button.setStyleSheet("#profile_button {\n"
            "color: #959595; }")
    def on_profile_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.profile_button.setStyleSheet("#profile_button {\n"
            "color: white; }\n"
        )
        self.ui.reports_button.setStyleSheet("#reports_button {\n"
            "color: #959595; }")
        self.ui.manage_button.setStyleSheet("#manage_button {\n"
            "color: #959595; }")
        self.ui.generate_button.setStyleSheet("#generate_button {\n"
            "color: #959595; }")
        self.ui.dashboard_button.setStyleSheet("#dashboard_button {\n"
            "color: #959595; }")


    # irename pod guro ning mga button rald, unsa man ning "pushButton_2"
    def on_calculate_button_clicked(self):
        global p_kwh 
        self.p_kwh = 0.6232
        self.amountDue = self.p_kwh * 99 #placeholder
        self.ui.billDue_edit.setText("₱ " + str(format(self.amountDue, "3.3f")))

    def on_profileEdit_button_pressed(self):
        self.ui.profileEdit_button.setCheckable(True)

        if not self.ui.profileEdit_button.isChecked(): #Checks if button has already been clicked to edit
            self.ui.adminID_edit.setReadOnly(False)
            self.ui.name_edit.setReadOnly(False)
            self.ui.adrress_edit.setReadOnly(False)
            self.ui.contactNo_edit.setReadOnly(False)
            self.ui.email_edit.setReadOnly(False)
            self.ui.password_edit.setReadOnly(False)
            self.ui.profileEdit_button.setText("Done")

        else:                              #if button has already been clicked to edit it puts it all back in read only
            self.ui.adminID_edit.setReadOnly(True)
            self.ui.name_edit.setReadOnly(True)
            self.ui.adrress_edit.setReadOnly(True)
            self.ui.contactNo_edit.setReadOnly(True)
            self.ui.email_edit.setReadOnly(True)
            self.ui.password_edit.setReadOnly(True)
            self.ui.profileEdit_button.setText("Edit")


        

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
