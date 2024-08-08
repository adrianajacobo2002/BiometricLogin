# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logindesignQUerFm.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(669, 442)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 671, 501))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.517, y2:0.602273, stop:0 rgba(178, 42, 52, 255), stop:1 rgba(246, 156, 156, 255));}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 80, 271, 61))
        self.label.setStyleSheet(u"font: 700 35pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.txtEmail = QLineEdit(self.widget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(190, 210, 291, 41))
        self.txtEmail.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 190, 131, 16))
        self.label_2.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnFacial = QPushButton(self.widget)
        self.btnFacial.setObjectName(u"btnFacial")
        self.btnFacial.setGeometry(QRect(200, 340, 261, 51))
        self.btnFacial.setStyleSheet(u"font: 10pt \"Nirmala UI\";\n"
"background-color: rgb(217, 43, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px\n"
"")
        self.btnVoice = QPushButton(self.widget)
        self.btnVoice.setObjectName(u"btnVoice")
        self.btnVoice.setGeometry(QRect(200, 280, 261, 51))
        self.btnVoice.setStyleSheet(u"font: 10pt \"Nirmala UI\";\n"
"background-color: rgb(242, 92, 120);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px")

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Login", u"Inicia Sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Correo Electr\u00f3nico", None))
        self.btnFacial.setText(QCoreApplication.translate("Login", u" Iniciar Sesi\u00f3n por Reconocimiento Facial", None))
        self.btnVoice.setText(QCoreApplication.translate("Login", u"Iniciar Sesi\u00f3n por  Reconocimiento de Voz", None))
    # retranslateUi

