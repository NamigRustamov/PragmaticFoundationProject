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
        self.label.setGeometry(QRect(60, 30, 61, 31))
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(219, 226, 223);")
        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 70, 781, 521))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 30, 93, 29))
        self.pushButton.setFont(font)
        self.verticalScrollBar = QScrollBar(Widget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(780, 70, 16, 521))
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Widget", u" Qal\u0131q", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Se\u00e7", None))
    # retranslateUi

