import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font


class side_bar(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.button_style = "color: black; background-color: #D3D3D3; border: none; outline: none;"
        self.current_dir = os.path.dirname(__file__)
        self.main_layout.setContentsMargins(0, 0, 0, 0)  # Left, Top, Right, Bottom margins
        self.main_layout.setSpacing(0)  # Spacing between widgets

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.hiden_bar_setup()
        self.shown_bar_setup()
        self.menu_setup()
        self.setup_main_layout()

    def hiden_bar_setup(self):
        self.hiden_bar = QWidget()
        self.hiden_bar.show()
        self.hiden_bar_layout = QVBoxLayout(self.hiden_bar)
        self.hiden_bar.setFixedWidth(70)
        self.setStyleSheet("background-color: #D3D3D3;")

        self.h_home_button = QPushButton("")
        self.h_home_button.setStyleSheet(self.button_style)
        self.home_icon = QIcon(os.path.join(os.path.dirname(self.current_dir), "icons/homeicon.png"))
        self.h_home_button.setIcon(self.home_icon)
        self.h_home_button.setIconSize(self.h_home_button.sizeHint() * 2)
        self.h_home_button.setFixedSize(60,60)

        self.h_table_button = QPushButton("")
        self.h_table_button.setStyleSheet(self.button_style)
        self.table_icon = QIcon(os.path.join(os.path.dirname(self.current_dir), "icons/tableicon.png"))
        self.h_table_button.setIcon(self.table_icon)
        self.h_table_button.setIconSize(self.h_table_button.sizeHint() * 2)
        self.h_table_button.setFixedSize(60,60)


        # setup logo
        self.logo = QLabel()
        self.logo_dir = os.path.join(os.path.dirname(self.current_dir), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)
        self.setup_logo()

        self.hiden_bar_layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        self.hiden_bar_layout.addWidget(self.h_home_button, alignment=Qt.AlignCenter)
        self.hiden_bar_layout.addWidget(self.h_table_button, alignment=Qt.AlignCenter)
        self.hiden_bar_layout.addStretch()

    def shown_bar_setup(self):
        self.shown_bar = QWidget()
        self.shown_bar.hide()
        self.shown_bar_layout = QVBoxLayout(self.shown_bar)
        self.shown_bar.setFixedWidth(150)
        self.setStyleSheet("background-color: #D3D3D3;")

        self.s_home_button = QPushButton("Home")
        self.s_home_button.setFont(self.font)
        self.s_home_button.setStyleSheet(self.button_style)
        self.s_home_button.setIcon(self.home_icon)
        self.s_home_button.setIconSize(self.s_home_button.sizeHint() * 2)
        self.s_home_button.setFixedSize(110,60)

        self.s_table_button = QPushButton("Table")
        self.s_table_button.setFont(self.font)
        self.s_table_button.setStyleSheet(self.button_style)
        self.s_table_button.setIcon(self.table_icon)
        self.s_table_button.setIconSize(self.s_table_button.sizeHint() * 2)
        self.s_table_button.setFixedSize(115,60)

        # setup logo 2
        self.logo_2 = QLabel()
        self.jeni_label = QLabel("J.E.N.I")
        self.jeni_label.setFont(self.font)
        self.jeni_label.setFixedSize(90,60)
        self.setup_logo_2()
        self.logo_w_text = QFrame()
        self.logo_w_text_layout = QHBoxLayout(self.logo_w_text)
        self.logo_w_text_layout.addWidget(self.logo_2)
        self.logo_w_text_layout.addWidget(self.jeni_label)


        self.shown_bar_layout.addWidget(self.logo_w_text, alignment=Qt.AlignLeft)
        self.shown_bar_layout.addWidget(self.s_home_button, alignment=Qt.AlignLeft)
        self.shown_bar_layout.addWidget(self.s_table_button, alignment=Qt.AlignLeft)
        self.shown_bar_layout.addStretch()

    def menu_setup(self):
        self.menu_button = QPushButton("")
        self.menu_button.setStyleSheet("background-color: white; border: none; outline: none;")
        self.menu_icon = QIcon(os.path.join(os.path.dirname(self.current_dir), "icons/menuicon.png"))
        self.menu_button.setIcon(self.menu_icon)
        self.menu_button.setIconSize(self.menu_button.sizeHint() * 2)
        self.menu_button.setFixedSize(60,60)


    def setup_logo(self):#set up logo img
        '''
        function to set up the logo for the customer window.
        '''
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(60, 60, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

    def setup_logo_2(self):#set up logo img
        '''
        function to set up the logo for the customer window.
        '''
        self.logo_2.setPixmap(self.pixmap)
        self.logo_2.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap_2 = self.pixmap.scaled(60, 60, aspectRatioMode=1)  # width, height
        self.logo_2.setPixmap(self.scaled_pixmap)
        self.logo_2.setStyleSheet("border: none;")

    def setup_main_layout(self):
        self.main_layout.addWidget(self.hiden_bar)
        self.main_layout.addWidget(self.shown_bar)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config() 
    app = QApplication(sys.argv)
    window = side_bar()
    window.show()
    sys.exit(app.exec_())
