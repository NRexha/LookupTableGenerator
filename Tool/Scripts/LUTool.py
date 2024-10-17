import sys
from PySide6.QtWidgets import QApplication
from ui_handler import UIHandler
from lut_generator import LUTGenerator

class LUTApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_handler = UIHandler()
        self.lut_generator = LUTGenerator(self.ui_handler)

    def run(self):
        self.ui_handler.show()
        sys.exit(self.app.exec())

if __name__ == '__main__':
    app = LUTApp()
    app.run()
