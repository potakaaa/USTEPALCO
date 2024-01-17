# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dashboard2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dashboard_Window(object):
    def setupUi(self, Dashboard_Window):
        Dashboard_Window.setObjectName("Dashboard_Window")
        Dashboard_Window.resize(922, 688)
        Dashboard_Window.setMinimumSize(QtCore.QSize(915, 688))
        Dashboard_Window.setMaximumSize(QtCore.QSize(1280, 895))
        Dashboard_Window.setStyleSheet("QMainWindow {\n"
"    background-color: #1C1C1C;\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(Dashboard_Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setMinimumSize(QtCore.QSize(0, 0))
        self.sidebar.setStyleSheet("*{\n"
"    margin: 0;\n"
"}\n"
"\n"
"#sidebar {\n"
"    background-color: #2B2B2B;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"#logo {\n"
"\n"
"}\n"
"\n"
"#logo_text {\n"
"    color: #D0F565;\n"
"    \n"
"}\n"
"\n"
"#dashboard_logo {\n"
"    margin-top: 20px;\n"
"    margin-left: 15px;\n"
"}\n"
"\n"
"\n"
"#reports_logo {\n"
"    margin-top: 20px;\n"
"    margin-left: 16px;\n"
"}\n"
"\n"
"#manage_logo {\n"
"    margin-top: 20px;\n"
"    margin-left: 12px;\n"
"}\n"
"\n"
"#generate_logo {\n"
"    margin-top: 20px;\n"
"    margin-left: 12px;\n"
"}\n"
"\n"
"\n"
"#profile_logo {\n"
"    margin-top: 20px;\n"
"    margin-left: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    margin-top: 20px;\n"
"    width: 5px;\n"
"    height: 25px;\n"
"    color: #FFFFFF;\n"
"    padding-left: 11px;\n"
"    text-align: left;\n"
"    background-color: transparent;\n"
"    \n"
"}\n"
"\n"
"#logout_button {\n"
"    height: 33px;\n"
"    background-color: #CAFF33;\n"
"    color: #1C1C1C;\n"
"    margin: 0px 11px 30px 11px;\n"
"    border-radius: 11px;\n"
"    padding: 0;\n"
"    text-align: center;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 20, 3, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.sidebar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(50, 50))
        self.logo.setMaximumSize(QtCore.QSize(30, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/pics/—Pngtree—lightning-icon-electric-logo_8832878.ico"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.logo_text = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logo_text.setFont(font)
        self.logo_text.setObjectName("logo_text")
        self.horizontalLayout.addWidget(self.logo_text)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dashboard_logo = QtWidgets.QLabel(self.sidebar)
        self.dashboard_logo.setMaximumSize(QtCore.QSize(40, 50))
        self.dashboard_logo.setText("")
        self.dashboard_logo.setPixmap(QtGui.QPixmap(":/icons/ui icons/Vector123.svg"))
        self.dashboard_logo.setObjectName("dashboard_logo")
        self.horizontalLayout_2.addWidget(self.dashboard_logo)
        self.dashboard_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.dashboard_button.setFont(font)
        self.dashboard_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dashboard_button.setObjectName("dashboard_button")
        self.horizontalLayout_2.addWidget(self.dashboard_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reports_logo = QtWidgets.QLabel(self.sidebar)
        self.reports_logo.setMaximumSize(QtCore.QSize(40, 50))
        self.reports_logo.setText("")
        self.reports_logo.setPixmap(QtGui.QPixmap(":/icons/ui icons/Vector.svg"))
        self.reports_logo.setObjectName("reports_logo")
        self.horizontalLayout_3.addWidget(self.reports_logo)
        self.reports_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.reports_button.setFont(font)
        self.reports_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reports_button.setObjectName("reports_button")
        self.horizontalLayout_3.addWidget(self.reports_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.manage_logo = QtWidgets.QLabel(self.sidebar)
        self.manage_logo.setMaximumSize(QtCore.QSize(40, 50))
        self.manage_logo.setText("")
        self.manage_logo.setPixmap(QtGui.QPixmap(":/icons/ui icons/Icon.svg"))
        self.manage_logo.setObjectName("manage_logo")
        self.horizontalLayout_4.addWidget(self.manage_logo)
        self.manage_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.manage_button.setFont(font)
        self.manage_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manage_button.setObjectName("manage_button")
        self.horizontalLayout_4.addWidget(self.manage_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.generate_logo = QtWidgets.QLabel(self.sidebar)
        self.generate_logo.setMaximumSize(QtCore.QSize(40, 50))
        self.generate_logo.setText("")
        self.generate_logo.setPixmap(QtGui.QPixmap(":/icons/ui icons/basil_invoice-solid.svg"))
        self.generate_logo.setObjectName("generate_logo")
        self.horizontalLayout_5.addWidget(self.generate_logo)
        self.generate_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.generate_button.setFont(font)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout_5.addWidget(self.generate_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.profile_logo = QtWidgets.QLabel(self.sidebar)
        self.profile_logo.setMaximumSize(QtCore.QSize(40, 50))
        self.profile_logo.setText("")
        self.profile_logo.setPixmap(QtGui.QPixmap(":/icons/ui icons/mdi_clipboard-user.svg"))
        self.profile_logo.setObjectName("profile_logo")
        self.horizontalLayout_6.addWidget(self.profile_logo)
        self.profile_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.profile_button.setFont(font)
        self.profile_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.profile_button.setObjectName("profile_button")
        self.horizontalLayout_6.addWidget(self.profile_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.logout_button = QtWidgets.QPushButton(self.sidebar)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout.addWidget(self.logout_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addWidget(self.sidebar)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.page_1.setFont(font)
        self.page_1.setStyleSheet("QLabel {\n"
"    color: #D0F565;\n"
"}\n"
"\n"
"#pages_text {\n"
"    margin-left: 20px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"#mainDashboard_text {\n"
"    margin-left: 18px;\n"
"}")
        self.page_1.setObjectName("page_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.header1 = QtWidgets.QVBoxLayout()
        self.header1.setSpacing(0)
        self.header1.setObjectName("header1")
        self.pages_text = QtWidgets.QLabel(self.page_1)
        self.pages_text.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        self.pages_text.setFont(font)
        self.pages_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pages_text.setObjectName("pages_text")
        self.header1.addWidget(self.pages_text)
        self.mainDashboard_text = QtWidgets.QLabel(self.page_1)
        self.mainDashboard_text.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mainDashboard_text.setFont(font)
        self.mainDashboard_text.setObjectName("mainDashboard_text")
        self.header1.addWidget(self.mainDashboard_text)
        self.body = QtWidgets.QFrame(self.page_1)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.gridLayout = QtWidgets.QGridLayout(self.body)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.body)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.header1.addWidget(self.body)
        self.gridLayout_2.addLayout(self.header1, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.dashboard_page = QtWidgets.QWidget()
        self.dashboard_page.setStyleSheet("QLabel {\n"
"    color: #D0F565;\n"
"}\n"
"\n"
"#pages_text2 {\n"
"    margin-left: 7px;\n"
"}\n"
"\n"
"#mainDashboard_text2 {\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.dashboard_page.setObjectName("dashboard_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dashboard_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.header = QtWidgets.QFrame(self.dashboard_page)
        self.header.setMaximumSize(QtCore.QSize(16777215, 80))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pages_text2 = QtWidgets.QLabel(self.header)
        self.pages_text2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        self.pages_text2.setFont(font)
        self.pages_text2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pages_text2.setObjectName("pages_text2")
        self.verticalLayout_4.addWidget(self.pages_text2)
        self.mainDashboard_text2 = QtWidgets.QLabel(self.header)
        self.mainDashboard_text2.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.mainDashboard_text2.setFont(font)
        self.mainDashboard_text2.setObjectName("mainDashboard_text2")
        self.verticalLayout_4.addWidget(self.mainDashboard_text2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.header)
        self.dashboard_body = QtWidgets.QFrame(self.dashboard_page)
        self.dashboard_body.setStyleSheet("#body2 {\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: 1px solid #D0F565;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#frame_4, #frame_5, #frame_6 {\n"
"    margin: 10px 2px 3px 10px;\n"
"}\n"
"\n"
"#frame_7, #frame_8 {\n"
"    margin: 10px 5px 3px 10px;\n"
"}\n"
"\n"
"#frame_9 {\n"
"    margin: 10px 5px 10px 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.dashboard_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard_body.setObjectName("dashboard_body")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dashboard_body)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.dashboard_body)
        self.frame_4.setMinimumSize(QtCore.QSize(160, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.dashboard_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(160, 70))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.dashboard_body)
        self.frame_6.setMinimumSize(QtCore.QSize(160, 70))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8.addWidget(self.frame_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_7 = QtWidgets.QFrame(self.dashboard_body)
        self.frame_7.setMinimumSize(QtCore.QSize(420, 160))
        self.frame_7.setMaximumSize(QtCore.QSize(1500, 300))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.dashboard_body)
        self.frame_8.setMinimumSize(QtCore.QSize(230, 160))
        self.frame_8.setMaximumSize(QtCore.QSize(400, 300))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9.addWidget(self.frame_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.frame_9 = QtWidgets.QFrame(self.dashboard_body)
        self.frame_9.setMinimumSize(QtCore.QSize(670, 100))
        self.frame_9.setMaximumSize(QtCore.QSize(1500, 16777215))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3.addWidget(self.frame_9)
        self.verticalLayout_6.addWidget(self.dashboard_body)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.generateBill_page = QtWidgets.QWidget()
        self.generateBill_page.setStyleSheet("QLabel {\n"
"    color: #D0F565;\n"
"}\n"
"\n"
"#pages_text_3 {\n"
"    margin-left: 7px;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"#mainDashboard_text_3 {\n"
"    margin-left: 5px;\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"#generateBill_frame {\n"
"    vertical-align: top;\n"
"    background-color: #2A2A2A;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    margin: 0px 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    margin-top: 3px;\n"
"    margin-left: 6px;\n"
"}\n"
"\n"
"#calculateBill_label {\n"
"    margin-top: 15px;\n"
"    margin-left: 8px;\n"
"}\n"
"\n"
"#conNum_label {\n"
"    margin-top: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    margin: 5px;\n"
"    background-color: #CAFF33;\n"
"    color: #2A2A2A;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #2A2A2A;\n"
"    color: #CAFF33;\n"
"}\n"
"\n"
"")
        self.generateBill_page.setObjectName("generateBill_page")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.generateBill_page)
        self.verticalLayout_16.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.header_2 = QtWidgets.QFrame(self.generateBill_page)
        self.header_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.header_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_2.setObjectName("header_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.header_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pages_text_3 = QtWidgets.QLabel(self.header_2)
        self.pages_text_3.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        self.pages_text_3.setFont(font)
        self.pages_text_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pages_text_3.setObjectName("pages_text_3")
        self.verticalLayout_8.addWidget(self.pages_text_3)
        self.generateBill_text_3 = QtWidgets.QLabel(self.header_2)
        self.generateBill_text_3.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.generateBill_text_3.setFont(font)
        self.generateBill_text_3.setObjectName("generateBill_text_3")
        self.verticalLayout_8.addWidget(self.generateBill_text_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_16.addWidget(self.header_2)
        self.generateBill_body = QtWidgets.QFrame(self.generateBill_page)
        self.generateBill_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generateBill_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generateBill_body.setObjectName("generateBill_body")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.generateBill_body)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.generateBill_frame = QtWidgets.QFrame(self.generateBill_body)
        self.generateBill_frame.setMaximumSize(QtCore.QSize(16777215, 400))
        self.generateBill_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generateBill_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generateBill_frame.setObjectName("generateBill_frame")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.generateBill_frame)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.calculateBill_label = QtWidgets.QLabel(self.generateBill_frame)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calculateBill_label.setFont(font)
        self.calculateBill_label.setObjectName("calculateBill_label")
        self.verticalLayout_15.addWidget(self.calculateBill_label)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.conNum_label = QtWidgets.QLabel(self.generateBill_frame)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        font.setWeight(75)
        self.conNum_label.setFont(font)
        self.conNum_label.setObjectName("conNum_label")
        self.verticalLayout_9.addWidget(self.conNum_label)
        self.conNum_edit = QtWidgets.QLineEdit(self.generateBill_frame)
        self.conNum_edit.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.conNum_edit.setFont(font)
        self.conNum_edit.setObjectName("conNum_edit")
        self.verticalLayout_9.addWidget(self.conNum_edit)
        self.verticalLayout_15.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fullName_label = QtWidgets.QLabel(self.generateBill_frame)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        font.setWeight(75)
        self.fullName_label.setFont(font)
        self.fullName_label.setObjectName("fullName_label")
        self.verticalLayout_11.addWidget(self.fullName_label)
        self.fullName_edit = QtWidgets.QLineEdit(self.generateBill_frame)
        self.fullName_edit.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.fullName_edit.setFont(font)
        self.fullName_edit.setObjectName("fullName_edit")
        self.verticalLayout_11.addWidget(self.fullName_edit)
        self.verticalLayout_15.addLayout(self.verticalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.dueDate_label = QtWidgets.QLabel(self.generateBill_frame)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        font.setWeight(75)
        self.dueDate_label.setFont(font)
        self.dueDate_label.setObjectName("dueDate_label")
        self.verticalLayout_12.addWidget(self.dueDate_label)
        self.dueDate_edit = QtWidgets.QLineEdit(self.generateBill_frame)
        self.dueDate_edit.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.dueDate_edit.setFont(font)
        self.dueDate_edit.setObjectName("dueDate_edit")
        self.verticalLayout_12.addWidget(self.dueDate_edit)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pesokwh_label = QtWidgets.QLabel(self.generateBill_frame)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pesokwh_label.setFont(font)
        self.pesokwh_label.setObjectName("pesokwh_label")
        self.verticalLayout_13.addWidget(self.pesokwh_label)
        self.pesokwh_edit = QtWidgets.QLineEdit(self.generateBill_frame)
        self.pesokwh_edit.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.pesokwh_edit.setFont(font)
        self.pesokwh_edit.setReadOnly(True)
        self.pesokwh_edit.setObjectName("pesokwh_edit")
        self.verticalLayout_13.addWidget(self.pesokwh_edit)
        self.horizontalLayout_10.addLayout(self.verticalLayout_13)
        self.verticalLayout_15.addLayout(self.horizontalLayout_10)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.billDue_label = QtWidgets.QLabel(self.generateBill_frame)
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setBold(True)
        font.setWeight(75)
        self.billDue_label.setFont(font)
        self.billDue_label.setObjectName("billDue_label")
        self.verticalLayout_14.addWidget(self.billDue_label)
        self.billDue_edit = QtWidgets.QLineEdit(self.generateBill_frame)
        self.billDue_edit.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        self.billDue_edit.setFont(font)
        self.billDue_edit.setReadOnly(True)
        self.billDue_edit.setObjectName("billDue_edit")
        self.verticalLayout_14.addWidget(self.billDue_edit)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.print_button = QtWidgets.QPushButton(self.generateBill_frame)
        self.print_button.setMinimumSize(QtCore.QSize(135, 47))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.print_button.setFont(font)
        self.print_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.print_button.setObjectName("print_button")
        self.horizontalLayout_11.addWidget(self.print_button)
        self.calculate_button = QtWidgets.QPushButton(self.generateBill_frame)
        self.calculate_button.setMinimumSize(QtCore.QSize(135, 47))
        font = QtGui.QFont()
        font.setFamily("DM Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_button.setFont(font)
        self.calculate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_button.setObjectName("calculate_button")
        self.horizontalLayout_11.addWidget(self.calculate_button)
        self.verticalLayout_15.addLayout(self.horizontalLayout_11)
        self.verticalLayout_17.addWidget(self.generateBill_frame)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_17.addItem(spacerItem3)
        self.verticalLayout_16.addWidget(self.generateBill_body)
        self.stackedWidget.addWidget(self.generateBill_page)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        Dashboard_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dashboard_Window)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dashboard_Window)

    def retranslateUi(self, Dashboard_Window):
        _translate = QtCore.QCoreApplication.translate
        Dashboard_Window.setWindowTitle(_translate("Dashboard_Window", "Dashboard"))
        self.logo_text.setText(_translate("Dashboard_Window", "USTEPALCO"))
        self.dashboard_button.setText(_translate("Dashboard_Window", "Dashboard"))
        self.reports_button.setText(_translate("Dashboard_Window", "Reports"))
        self.manage_button.setText(_translate("Dashboard_Window", "Manage Users"))
        self.generate_button.setText(_translate("Dashboard_Window", "Generate Bill"))
        self.profile_button.setText(_translate("Dashboard_Window", "Profile"))
        self.logout_button.setText(_translate("Dashboard_Window", "Logout"))
        self.pages_text.setText(_translate("Dashboard_Window", "Pages / Dashboard"))
        self.mainDashboard_text.setText(_translate("Dashboard_Window", "Main Dashboard"))
        self.label_3.setText(_translate("Dashboard_Window", "Merry Christmas!!!"))
        self.pages_text2.setText(_translate("Dashboard_Window", "Pages / Dashboard"))
        self.mainDashboard_text2.setText(_translate("Dashboard_Window", "Main Dashboard"))
        self.pages_text_3.setText(_translate("Dashboard_Window", "Pages / Generate"))
        self.generateBill_text_3.setText(_translate("Dashboard_Window", "Generate Bill"))
        self.calculateBill_label.setText(_translate("Dashboard_Window", "Calculate Bill"))
        self.conNum_label.setText(_translate("Dashboard_Window", "Contract Number"))
        self.conNum_edit.setPlaceholderText(_translate("Dashboard_Window", "ex. 926088"))
        self.fullName_label.setText(_translate("Dashboard_Window", "Full Name"))
        self.fullName_edit.setPlaceholderText(_translate("Dashboard_Window", "ex. Hans Del Mundo"))
        self.dueDate_label.setText(_translate("Dashboard_Window", "Due Date"))
        self.dueDate_edit.setPlaceholderText(_translate("Dashboard_Window", "mm-dd-yy"))
        self.pesokwh_label.setText(_translate("Dashboard_Window", "Peso per kWh"))
        self.pesokwh_edit.setPlaceholderText(_translate("Dashboard_Window", "₱ 0.6232"))
        self.billDue_label.setText(_translate("Dashboard_Window", "Bill Due"))
        self.print_button.setText(_translate("Dashboard_Window", "Print"))
        self.calculate_button.setText(_translate("Dashboard_Window", "Calculate"))
import resource_rc_rc