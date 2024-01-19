import random
import sys, sqlite3, hashlib
from pages.mailer import Mail
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pages.login_page import Ui_MainWindow as LoginPage
from pages.dashboard2 import Ui_Dashboard_Window as DashboardPage
from pages.pdfreceipt import PDF_receipt
from datetime import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__seed = "USTEPALCO"
        self.__db_file = "USTEPALCO.db"
        self.__conn = sqlite3.connect(self.__db_file)
        self.__sql = self.__conn.cursor()
        self.__session_admin_uid = 0
        self.page_view('login')
        global p_kwh 
        self.p_kwh = 11.3997


    def on_dashboard_button_pressed(self):
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
        
    def on_reports_button_pressed(self):
        self.ui.stackedWidget.setCurrentIndex(2)

        self.__users = [self.ui.paymentUsers_row1, self.ui.paymentUsers_row2, 
                        self.ui.paymentUsers_row3, self.ui.paymentUsers_row4, 
                        self.ui.paymentUsers_row5, self.ui.paymentUsers_row6, 
                        self.ui.paymentUsers_row7, self.ui.paymentUsers_row8]
        self.__ad = [self.ui.paymentAddress_row1, self.ui.paymentAddress_row2, 
                        self.ui.paymentAddress_row3, self.ui.paymentAddress_row4, 
                        self.ui.paymentAddress_row5, self.ui.paymentAddress_row6, 
                        self.ui.paymentAddress_row7, self.ui.paymentAddress_row8]
        self.__dates = [self.ui.paymentDate_row1, self.ui.paymentDate_row2, 
                        self.ui.paymentDate_row3, self.ui.paymentDate_row4, 
                        self.ui.paymentDate_row5, self.ui.paymentDate_row6, 
                        self.ui.paymentDate_row7, self.ui.paymentDate_row8]
        self.__usage = [self.ui.paymentAmount_row1, self.ui.paymentAmount_row2, 
                        self.ui.paymentAmount_row3, self.ui.paymentAmount_row4, 
                        self.ui.paymentAmount_row5, self.ui.paymentAmount_row6, 
                        self.ui.paymentAmount_row7, self.ui.paymentAmount_row8]
        
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
        
        self.__sql.execute("SELECT * FROM payment_det ORDER BY date_payment DESC;")

        for i in range(len(self.__users)):
            
            self.__sql.execute("SELECT full_name FROM payment_det")
            namcong = self.__sql.fetchall()

            self.__users[i].setText(str(namcong[i])[2:len(str(namcong[i])) - 3])

            self.__sql.execute("SELECT address FROM payment_det")
            adcong = self.__sql.fetchall()
            self.__ad[i].setText(str(adcong[i])[2:len(str(adcong[i])) - 3])

            self.__sql.execute("SELECT date_payment FROM payment_det")
            datcong = self.__sql.fetchall()
            self.__dates[i].setText(str(datcong[i])[2:len(str(datcong[i])) - 3])

            self.__sql.execute("SELECT usage FROM payment_det")
            usagcong = self.__sql.fetchall()

            usag = int(str(usagcong[i])[1:len(str(usagcong[i])) - 2]) * self.p_kwh
            self.__usage[i].setText("₱ "+ str(format(usag, "3.3f")))  

    def on_manage_button_pressed(self):
        
        self.ui.stackedWidget.setCurrentIndex(3)

        self.__names = [self.ui.row1_name, self.ui.row1_name_2, self.ui.row1_name_3, self.ui.row2_name, 
                    self.ui.row2_name_2, self.ui.row2_name_3, self.ui.row3_name, self.ui.row3_name_2, 
                    self.ui.row3_name_3, self.ui.row4_name, self.ui.row4_name_2, self.ui.row4_name_3,
                    self.ui.row5_name, self.ui.row5_name_2, self.ui.row5_name_3, self.ui.row6_name, 
                    self.ui.row6_name_2, self.ui.row6_name_3]
            
        self.__address = [self.ui.row1_address, self.ui.row1_address_2, self.ui.row1_address_3, self.ui.row2_address, 
                    self.ui.row2_address_2, self.ui.row2_address_3, self.ui.row3_address, self.ui.row3_address_2, 
                    self.ui.row3_address_3, self.ui.row4_address, self.ui.row4_address_2, self.ui.row4_address_3,
                    self.ui.row5_address, self.ui.row5_address_2, self.ui.row5_address_3, self.ui.row6_address, 
                    self.ui.row6_address_2, self.ui.row6_address_3]
            
        self.__contractNo = [self.ui.row1_contractNo, self.ui.row1_contractNo_2, self.ui.row1_contractNo_3, self.ui.row2_contractNo, 
                    self.ui.row2_contractNo_2, self.ui.row2_contractNo_3, self.ui.row3_contractNo, self.ui.row3_contractNo_2, 
                    self.ui.row3_contractNo_3, self.ui.row4_contractNo, self.ui.row4_contractNo_2, self.ui.row4_contractNo_3,
                    self.ui.row5_contractNo, self.ui.row5_contractNo_2, self.ui.row5_contractNo_3, self.ui.row6_contractNo, 
                    self.ui.row6_contractNo_2, self.ui.row6_contractNo_3]

        self.__amount = [self.ui.row1_amount, self.ui.row1_amount_2, self.ui.row1_amount_3, self.ui.row2_amount, 
                    self.ui.row2_amount_2, self.ui.row2_amount_3, self.ui.row3_amount, self.ui.row3_amount_2, 
                    self.ui.row3_amount_3, self.ui.row4_amount, self.ui.row4_amount_2, self.ui.row4_amount_3,
                    self.ui.row5_amount, self.ui.row5_amount_2, self.ui.row5_amount_3, self.ui.row6_amount, 
                    self.ui.row6_amount_2, self.ui.row6_amount_3]
        
        self.ui.users_StackedWidget.setCurrentIndex(0)

        for i in range(len(self.__names)):
            
            self.__sql.execute("SELECT full_name FROM users")
            namcon = self.__sql.fetchall()
            self.__names[i].setText(str(namcon[i])[2:len(str(namcon[i])) - 3])

            self.__sql.execute("SELECT address FROM users")
            adcon = self.__sql.fetchall()
            self.__address[i].setText(str(adcon[i])[2:len(str(adcon[i])) - 3])

            self.__sql.execute("SELECT contract_No FROM users")
            concon = self.__sql.fetchall()
            self.__contractNo[i].setText(str(concon[i])[2:len(str(concon[i])) - 3])

            self.__sql.execute("SELECT amount_due FROM users")
            amcon = self.__sql.fetchall()
            self.__amount[i].setText("₱ " + str(amcon[i])[1:len(str(amcon[i])) - 2])

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
    def on_generate_button_pressed(self):
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
        
    def on_profile_button_pressed(self):
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

        uid, admin_id, full_name, address, phone_no, email, password = self.__get_admin_data()
        self.ui.adminID_edit.setText(admin_id)
        self.ui.name_edit.setText(full_name)
        self.ui.adrress_edit.setText(address)
        self.ui.contactNo_edit.setText(phone_no)
        self.ui.email_edit.setText(email)
        self.ui.password_edit.setText("")
    
    def __get_admin_data(self):
        self.__sql.execute("SELECT * FROM admin WHERE uid = ?",(self.__session_admin_uid,))
        return self.__sql.fetchall()[0]


    def __check_login(self, email, password):
        password = self.secure_password(password) 
        self.__sql.execute("SELECT * FROM admin WHERE email = ? AND password = ?;",(email, password))
        results = self.__sql.fetchall()
        status = False # False default status means user not exists
        if(len(results) > 0):
            self.__session_admin_uid = results[0][0] # Store the admin uid in the session user uid. 
            status = True # Status change value to True if user exists

        return status
    
    def __update_password(self, new_password, email):
        new_password = self.secure_password(new_password)
        self.__sql.execute("UPDATE admin SET password = ? WHERE email = ?", (new_password, email))
        self.__conn.commit()
    
    def __is_Email_Exists(self, email):
        self.__sql.execute("SELECT * FROM admin WHERE email = ?", (email,))
        results = self.__sql.fetchall()
        if(len(results) > 0):
            return True
        return False

    def __get_user_usage(self, contract_no, fullname):
        self.__sql.execute("SELECT pd.usage FROM payment_det pd JOIN users u ON pd.uid = u.uid WHERE u.contract_no = ? AND u.full_name = ?", (contract_no, fullname ))
        results = self.__sql.fetchall()
        if(len(results) > 0):
            return results[0][0]

        self.show_message("ERROR", "Invalid contract!", QMessageBox.Warning)
        return 0
    
    def __get_user_print_data(self, contract_no, fullname):
        self.__sql.execute("SELECT * FROM payment_det pd JOIN users u ON pd.uid = u.uid WHERE u.contract_no = ? AND u.full_name = ?", (contract_no, fullname ))
        results = self.__sql.fetchall()
        if(len(results) > 0):
            return results
        return False
    
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
        if(self.__is_Email_Exists(email) == False):
            return
        temporary_password = self.generate_otp()
        user = (email.split("@")[0]).title()

        subject = "Password reset on USTEPALCO"
        content = f"""
        <div>
        <table style="width:100%; height: 40vh; font-size:14px; background-color: rgb(0,0,0,0.1); display:flex; align-items:center; justify-content: center;">
            <tr>
            <td>
            <div style="min-width:350px; font-family: sans-serif; background-color: rgb(255,255,255,0.6); padding:10px; border-radius:10px; box-shadow:0px 0px 5px 1px rgb(0,0,0,0.2);">
                <h2 style="font-family: sans-serif; text-align: center;">TEMPORARY PASSWORD</h2>
                <p>
                    Hey {user},<br>
                    A password reset was requested for your account. Below is your temporary password:
                </p>
                <div style="text-align: center;">
                    <input readonly value="{temporary_password}" style="border-radius:5px; padding:5px; font-family: sans-serif; text-align: center; color:black; font-size:28px; outline:none; border:1px solid black;">
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
        self.__update_password(temporary_password, email)

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
        email = self.ui.edit_email.text().strip()
        passw = self.ui.edit_password.text().strip()
        if((len(passw) < 8)):
            self.show_message("ERROR", "Minimum password length is 8.", QMessageBox.Warning)
        elif(self.__check_login(email, passw) ):
            self.page_view('dashboard')
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.dashboard_button.setStyleSheet("#dashboard_button {\n"
            "color: white; }\n"
        else:
            self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)

        # self.page_view('dashboard')
    
    def on_forget_button_pressed(self):
        email = self.ui.edit_email.text()
        if(email.strip() == ''):
            self.show_message("ERROR", "Please enter your email for password reset!", QMessageBox.Warning)
            return
        self.reset_password(email)

    def on_calculate_button_pressed(self):
        contract_no = self.ui.conNum_edit.text().strip()
        fullname = self.ui.fullName_edit.text().strip()
        usage = self.__get_user_usage(contract_no, fullname)

        self.amountDue = self.p_kwh * usage
        self.ui.billDue_edit.setText("₱ " + str(format(self.amountDue, "3.3f")))
    
    def on_print_button_pressed(self):
        current_date = datetime.now()
        contract_no = self.ui.conNum_edit.text().strip()
        fullname = self.ui.fullName_edit.text().strip()

        user_data  = self.__get_user_print_data(contract_no,fullname)
        if(user_data == False):
            self.show_message("ERROR", "Invalid contract!", QMessageBox.Warning)
            return
        user_data = user_data[0]
        fullname = user_data[1]
        address = user_data[2]
        usage = user_data[3]
        contract_no = user_data[8]
        date = str(current_date.strftime("%Y-%m-%d"))
        time = str(current_date.strftime("%I:%M %p"))
        transaction_number = random.randint(99999,999999)

        receipt_title = "Electricity_Bill_Receipt-" + date
        output_file = receipt_title+'.pdf'

        items = [
            (usage, self.p_kwh, (int(usage)*self.p_kwh))
        ]

        receipt = PDF_receipt(receipt_title, contract_no, fullname, address, transaction_number, date, time, items)
        receipt.generate(output_file)
        self.show_message("Success!", f"Receipt saved as {output_file}", QMessageBox.Information)



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

            admin_data = self.__get_admin_data()
            uid = admin_data[0]
            admin_id = self.ui.adminID_edit.text()
            fullname = self.ui.name_edit.text()
            address = self.ui.adrress_edit.text()
            contact_no = self.ui.contactNo_edit.text()
            email = self.ui.email_edit.text()
            password = self.ui.password_edit.text()
            if(password.strip() == ''):
                password = admin_data[-1]
            else:
                password = self.secure_password(password)
            self.__sql.execute("UPDATE admin SET admin_id = ?, full_name = ?, address = ?, phone_no = ?, email = ?, password = ? WHERE uid = ?",(admin_id, fullname, address, contact_no, email, password, uid))
            self.__conn.commit()

    def on_next_button_pressed(self):     
        nextwidg = self.ui.users_StackedWidget.currentIndex() + 1

        if nextwidg < 3:
            self.ui.users_StackedWidget.setCurrentIndex(nextwidg)
        else:
            self.ui.users_StackedWidget.setCurrentIndex(0)
        
        
if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
