# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QWidget)
import gui_main_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 600)
        MainWindow.setMouseTracking(True)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QWidget#mainwidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0.16, y1:0.705273, x2:1, y2:0, stop:0.477273 rgba(44, 44, 42, 255), stop:1 rgba(107, 129, 50, 255));\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_logo {\n"
"	image: url(:/icons/assets/icons/mp_to_litchi_icon.ico);\n"
"}\n"
"")
        self.mainwidget = QWidget(MainWindow)
        self.mainwidget.setObjectName(u"mainwidget")
        self.mainwidget.setEnabled(True)
        self.textBrowser_manual = QTextBrowser(self.mainwidget)
        self.textBrowser_manual.setObjectName(u"textBrowser_manual")
        self.textBrowser_manual.setGeometry(QRect(20, 110, 821, 421))
        self.textBrowser_manual.setMouseTracking(False)
        self.textBrowser_manual.setAcceptDrops(False)
        self.textBrowser_manual.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.layoutWidget = QWidget(self.mainwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 871, 91))
        self.horizontalLayout_header = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_header.setSpacing(6)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.horizontalLayout_header.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_header.setContentsMargins(10, 5, 0, 0)
        self.label_logo = QLabel(self.layoutWidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setScaledContents(False)
        self.label_logo.setMargin(32)
        self.label_logo.setIndent(-1)
        self.label_logo.setOpenExternalLinks(True)

        self.horizontalLayout_header.addWidget(self.label_logo)

        self.pushButton_home = QPushButton(self.layoutWidget)
        self.buttonGroup_header = QButtonGroup(MainWindow)
        self.buttonGroup_header.setObjectName(u"buttonGroup_header")
        self.buttonGroup_header.addButton(self.pushButton_home)
        self.pushButton_home.setObjectName(u"pushButton_home")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/bx-home-alt-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_home.setIcon(icon)
        self.pushButton_home.setIconSize(QSize(32, 32))
        self.pushButton_home.setAutoRepeat(False)
        self.pushButton_home.setAutoExclusive(False)
        self.pushButton_home.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton_home)

        self.pushButton_list = QPushButton(self.layoutWidget)
        self.buttonGroup_header.addButton(self.pushButton_list)
        self.pushButton_list.setObjectName(u"pushButton_list")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/bx-list-ul.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_list.setIcon(icon1)
        self.pushButton_list.setIconSize(QSize(32, 32))
        self.pushButton_list.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton_list)

        self.pushButton_settings = QPushButton(self.layoutWidget)
        self.buttonGroup_header.addButton(self.pushButton_settings)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/bx-cog.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_settings.setIcon(icon2)
        self.pushButton_settings.setIconSize(QSize(32, 32))
        self.pushButton_settings.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton_settings)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer)

        self.pushButton_minimize = QPushButton(self.layoutWidget)
        self.buttonGroup_header.addButton(self.pushButton_minimize)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/bx-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon3)
        self.pushButton_minimize.setIconSize(QSize(32, 32))
        self.pushButton_minimize.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton_minimize)

        self.pushButton_close = QPushButton(self.layoutWidget)
        self.buttonGroup_header.addButton(self.pushButton_close)
        self.pushButton_close.setObjectName(u"pushButton_close")
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/bx-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon4)
        self.pushButton_close.setIconSize(QSize(32, 32))
        self.pushButton_close.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton_close)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.mainwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_list.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser_manual.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Yu Gothic UI'; font-size:36pt; font-weight:700; color:#efeff1;\">	  How to use this application</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Yu Gothic UI'; font-size:36pt; font-weight:700; color:#efeff1;\"><br /></p>\n"
"<p style=\" margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Yu Gothic UI'; font-size:20pt; color:#efeff1;\">	1) Drop files into this window</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Yu Gothic UI'; font-size:20pt; color:#efeff1;\">	2) Step 2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Yu Gothic UI'; font-size:20pt; color:#efeff1;\">	3) Step 3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Yu Gothic UI'; font-size:20pt; color:#efeff1;\">	4) Step 4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font"
                        "-family:'Yu Gothic UI'; font-size:20pt; color:#efeff1;\">	5) Step 5</span></p></body></html>", None))
    # retranslateUi

