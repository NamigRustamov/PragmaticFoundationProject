
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
import sys




class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setGeometry(100,100,500,500)
        self.setWindowTitle("Satislar")
        self.setWindowIcon(QIcon('icons/qt.png'))
        self.setStyleSheet('background-color:blue')
        self.setWindowOpacity(0.7)


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())



