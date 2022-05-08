# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"background-color: rgb(170, 203, 255);")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 470, 93, 29))
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 390, 511, 26))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 430, 511, 26))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 390, 121, 20))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 430, 63, 20))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 320, 501, 31))
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 160, 301, 51))
        font3 = QFont()
        font3.setFamilies([u"Cambria"])
        font3.setPointSize(18)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Daxil olun", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0130stifad\u0259\u00e7i ad\u0131", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Parol", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Daxil olmaq \u00fc\u00e7\u00fcn qeydiyyatdan ke\u00e7in", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Ambara Xo\u015f G\u0259lmisiniz", None))
    # retranslateUi

