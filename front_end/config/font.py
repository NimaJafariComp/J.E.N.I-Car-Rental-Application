import os
from PyQt5.QtGui import QFontDatabase, QFont

class font:
    '''
    A class to set up the font for the gui.
    '''
    def __init__(self):
        '''
        Initializes the font from the tff file.
        '''
        # Construct the absolute path to the font file
        font_path = os.path.join(os.path.dirname(__file__), "fonts/Staatliches-Regular.ttf")
        
        # Load the font using the absolute path
        self.staaliches = QFontDatabase.addApplicationFont(font_path)
        
        # Check if the font was loaded successfully
        if self.staaliches == -1:
            raise ValueError(f"Failed to load font from {font_path}")

        # Get the font family name, if available
        font_families = QFontDatabase.applicationFontFamilies(self.staaliches)
        if not font_families:
            raise ValueError("No font families found for the loaded font")
        
        self.font_family = font_families[0]

