import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from project1 import Ui_Widget


class Widget (QWidget):
    def __init__(self):
        super(Widget,self).__init__()
        self.ui=Ui_Widget
        self.ui.setupUi(self)




if __name__ == "__main__":
    app=QApplication()
    main=Widget()
    main.show()
    sys.exit(app.exec())




