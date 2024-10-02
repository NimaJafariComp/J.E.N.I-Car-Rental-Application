from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QLabel

class font():
    def __init__(self):
        # Load the Staatliches font
        self.staaliches = QFontDatabase.addApplicationFont("fonts/Staatliches-Regular.ttf")
        
        # Get the font family name
        self.font_family = QFontDatabase.applicationFontFamilies(self.staaliches)[0]
        
    
