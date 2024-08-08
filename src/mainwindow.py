# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowwuFdtz.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 435)
        MainWindow.setStyleSheet(u"")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 741, 441))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.517, y2:0.602273, stop:0 rgba(178, 42, 52, 255), stop:1 rgba(246, 156, 156, 255));}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 100, 301, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(35)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 700 35pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(230, 200, 271, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy1)
        self.btnLogin.setStyleSheet(u"font: 14pt \"Nirmala UI\";\n"
"background-color: rgb(217, 43, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px\n"
"\n"
"")
        self.txtRegister = QLabel(self.widget)
        self.txtRegister.setObjectName(u"txtRegister")
        self.txtRegister.setGeometry(QRect(240, 270, 248, 22))
        sizePolicy.setHeightForWidth(self.txtRegister.sizePolicy().hasHeightForWidth())
        self.txtRegister.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(True)
        self.txtRegister.setFont(font1)
        self.txtRegister.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 12pt \"Nirmala UI\";")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login with Biometrics", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">BIENVENIDO</p></body></html>", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Inicia Sesi\u00f3n", None))
        self.txtRegister.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u00bfA\u00fan no tienes cuenta? \u00a1Reg\u00edstrate!</p></body></html>", None))
    # retranslateUi

