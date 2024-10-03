from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QScreen

class screen_setting():
    def __init__(self):
        super().__init__()

        # Get screen information
        self.screen = QApplication.primaryScreen()
        self.dpi = self.screen.logicalDotsPerInch()
        self.screen_ratio = self.dpi/96

    def print_dpi(self):
        print(f"Screen DPI: {self.dpi}")

