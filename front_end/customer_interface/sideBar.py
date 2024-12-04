import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font


class side_bar(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.button_style = "background-color: #D3D3D3; border: none; text-align: center"
        self.current_dir = os.path.dirname(__file__)

        self.hiden_bar_setup()
        self.setup_main_layout()

    def hiden_bar_setup(self):
        self.hiden_bar = QWidget()
        self.hiden_bar_layout = QVBoxLayout(self.hiden_bar)
        self.hiden_bar.setFixedWidth(65)
        self.hiden_bar.setFixedHeight(1000)
        self.setStyleSheet("background-color: #D3D3D3;")

        self.home_button = QPushButton("")
        self.home_button.setStyleSheet(self.button_style)
        self.home_icon = QIcon(os.path.join(os.path.dirname(self.current_dir), "icons/homeicon.png"))
        self.home_button.setIcon(self.home_icon)
        self.home_button.setIconSize(self.home_button.sizeHint() * 2)
        self.home_button.setFixedSize(60,60)

        self.table_button = QPushButton("")
        self.table_button.setStyleSheet(self.button_style)
        self.table_icon = QIcon(os.path.join(os.path.dirname(self.current_dir), "icons/tableicon.png"))
        self.table_button.setIcon(self.table_icon)
        self.table_button.setIconSize(self.table_button.sizeHint() * 2)
        self.table_button.setFixedSize(60,60)


        # setup logo
        self.logo = QLabel()
        self.current_dir = os.path.dirname(__file__)
        self.logo_dir = os.path.join(os.path.dirname(self.current_dir), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)
        self.setup_logo()

        self.hiden_bar_layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        self.hiden_bar_layout.addWidget(self.home_button, alignment=Qt.AlignCenter)
        self.hiden_bar_layout.addWidget(self.table_button, alignment=Qt.AlignCenter)
        self.hiden_bar_layout.addStretch()

        
    def setup_logo(self):#set up logo img
        '''
        function to set up the logo for the customer window.
        '''
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(60, 60, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

    def setup_main_layout(self):
        self.main_layout.addWidget(self.hiden_bar)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config() 
    app = QApplication(sys.argv)
    window = side_bar()
    window.show()
    sys.exit(app.exec_())
