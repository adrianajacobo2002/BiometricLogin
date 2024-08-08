# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerdesignIsfYfE.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(671, 536)
        Dialog.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.517, y2:0.602273, stop:0 rgba(178, 42, 52, 255), stop:1 rgba(246, 156, 156, 255));}")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 671, 541))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 60, 261, 71))
        self.label.setStyleSheet(u"font: 700 35pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 160, 81, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.txtName = QLineEdit(self.widget)
        self.txtName.setObjectName(u"txtName")
        self.txtName.setGeometry(QRect(140, 190, 171, 41))
        self.txtName.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 160, 81, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.txtLastName = QLineEdit(self.widget)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setGeometry(QRect(370, 190, 171, 41))
        self.txtLastName.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 250, 141, 16))
        self.label_4.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.txtEmail = QLineEdit(self.widget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(140, 270, 401, 41))
        self.txtEmail.setStyleSheet(u"font: 12pt \"Nirmala UI\";")
        self.btnFaceRecon = QPushButton(self.widget)
        self.btnFaceRecon.setObjectName(u"btnFaceRecon")
        self.btnFaceRecon.setGeometry(QRect(140, 350, 181, 51))
        self.btnFaceRecon.setStyleSheet(u"font: 10pt \"Nirmala UI\";\n"
"background-color: rgb(242, 92, 120);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px")
        self.btnVoiceRecon = QPushButton(self.widget)
        self.btnVoiceRecon.setObjectName(u"btnVoiceRecon")
        self.btnVoiceRecon.setGeometry(QRect(360, 350, 181, 51))
        self.btnVoiceRecon.setStyleSheet(u"font: 10pt \"Nirmala UI\";\n"
"background-color: rgb(242, 92, 120);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px")
        self.btnRegister = QPushButton(self.widget)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setGeometry(QRect(240, 430, 191, 51))
        self.btnRegister.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"background-color: rgb(217, 43, 90);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u00a1Reg\u00edstrate!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Apellido", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Correo Electr\u00f3nico", None))
        self.btnFaceRecon.setText(QCoreApplication.translate("Dialog", u"Identificar Rostro", None))
        self.btnVoiceRecon.setText(QCoreApplication.translate("Dialog", u"Identificar Voz", None))
        self.btnRegister.setText(QCoreApplication.translate("Dialog", u"Registrar", None))
    # retranslateUi

