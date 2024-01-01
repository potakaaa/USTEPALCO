from email.mime.text import MIMEText
from pages.encrypter import HaxPass
import smtplib, ssl

class Mail:
    def __init__(self, subject="", content="", content_type="plain"):
        self.__email = "ustepalco@gmail.com"
        self.__passw = HaxPass("5896642898799897497234238258654924945267355893439656954327372774885588583756622829533737593973398253567367632497927668633489475666224846443983442555957462778793452539887785227462846554895883356254574294549338872866388692692344632464668682343333977686696659293848784296688927336793736668924294539735329978987954")
        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 587

        self.subject = subject
        self.content = content
        self.content_type = content_type

    def sendto(self, target_mail):
        mail_pass = self.__passw.sh1ft()
        message = MIMEText(self.content, self.content_type)
        message["subject"] = self.subject
        message["from"] = "support@ustepalco.cloud"
        message["to"] = target_mail
        
        context = ssl.create_default_context()
        server = smtplib.SMTP(self.smtp_host, self.smtp_port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(self.__email, self.__passw.shlft(mail_pass))
        server.sendmail(self.__email, target_mail, message.as_string())
        server.quit()

