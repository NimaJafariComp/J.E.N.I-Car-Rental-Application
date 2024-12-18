from PyQt5.QtGui import QFont

class font:
    '''
    A class to set up the font for the gui.
    '''
    def __init__(self):
        '''
        Initializes the font using a built-in system font.
        '''
        # Use a standard built-in system font
        self.staaliches = "Arial"  # Replace with another common system font if needed
        
        # Check if the font is available
        if not QFont(self.staaliches).exactMatch():
            raise ValueError(f"The specified font '{self.staaliches}' is not available on this system")
        
        # Set the font family to the chosen font
        self.font_family = self.staaliches


