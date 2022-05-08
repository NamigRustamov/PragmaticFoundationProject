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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"background-color: rgb(170, 203, 255);")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 181, 51))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(31, 220, 161, 61))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(199, 220, 235, 61))
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(441, 220, 171, 61))
        self.pushButton_3.setFont(font1)
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(620, 220, 151, 61))
        self.pushButton_4.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"S\u0259n\u0259dl\u0259r", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"B\u00fct\u00fcn S\u0259n\u0259dl\u0259r", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Al\u0131\u015f S\u0259n\u0259dl\u0259ri \u0130N\n"
"(daxil olan materiallar)\n"
"", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u0130stifad\u0259y\u0259 \n"
"G\u00f6nd\u0259ril\u0259n OUT\n"
"Materiallar\u0131n\n"
"S\u0259n\u0259dl\u0259ri\n"
"", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Qal\u0131q", None))
    # retranslateUi

