# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homedesignaXRzmA.ui'
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

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(619, 451)
        self.widget = QWidget(Home)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 631, 451))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.517, y2:0.602273, stop:0 rgba(178, 42, 52, 255), stop:1 rgba(246, 156, 156, 255));}")
        self.txtName = QLabel(self.widget)
        self.txtName.setObjectName(u"txtName")
        self.txtName.setGeometry(QRect(180, 190, 291, 61))
        self.txtName.setStyleSheet(u"font: 700 35pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.txtLastName = QLabel(self.widget)
        self.txtLastName.setObjectName(u"txtLastName")
        self.txtLastName.setGeometry(QRect(210, 250, 231, 71))
        self.txtLastName.setStyleSheet(u"font: 700 35pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 140, 341, 41))
        self.label_3.setStyleSheet(u"font: 700 25pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnLogOut = QPushButton(self.widget)
        self.btnLogOut.setObjectName(u"btnLogOut")
        self.btnLogOut.setGeometry(QRect(510, 20, 91, 51))
        self.btnLogOut.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemShutdown))
        self.btnLogOut.setIcon(icon)
        self.btnLogOut.setIconSize(QSize(18, 18))
        self.btnLogOut.setCheckable(False)

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Dialog", None))
        self.txtName.setText(QCoreApplication.translate("Home", u"<html><head/><body><p align=\"center\">NOMBRE</p></body></html>", None))
        self.txtLastName.setText(QCoreApplication.translate("Home", u"<html><head/><body><p align=\"center\">APELLIDO</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Home", u"<html><head/><body><p align=\"center\">Bienvenido/a</p></body></html>", None))
        self.btnLogOut.setText("")
    # retranslateUi

