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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QPushButton,
    QScrollBar, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setStyleSheet(u"background-color: rgb(170, 203, 255);")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 364, 27))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(219, 226, 223);")
        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 80, 781, 511))
        self.verticalScrollBar = QScrollBar(Widget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(780, 80, 16, 511))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(560, 20, 193, 36))
        self.pushButton.setFont(font)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Al\u0131\u015f S\u0259n\u0259dl\u0259ri (daxil olan materiallar)", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Yeni s\u0259n\u0259d \u0259lav\u0259 et", None))
    # retranslateUi

