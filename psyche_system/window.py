# window.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class PsycheWindow(QMainWindow):
    def __init__(self, title="Psyche Window", width=800, height=600):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, width, height)
        self.initUI()

    def initUI(self):
        label = QLabel("Добро пожаловать в PsycheSystem!", self)
        label.move(50, 50)

    def create_window(self):
        app = QApplication(sys.argv)
        self.show()
        sys.exit(app.exec_())
