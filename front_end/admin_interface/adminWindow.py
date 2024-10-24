import os
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class admin_window(QWidget):
    def __init__(self):
        super().__init__()
        # setup admin window layout
        self.admin_layout = QVBoxLayout(self)

        # setup diffrent Qframes
        self.top_frame = QFrame()
        self.top_frame_layout = QHBoxLayout(self.top_frame)
        self.bottom_frame = QFrame()

        # setup other sub widgets
        self.customer_button = QPushButton("Customer")

        # set up logo
        self.logo = QLabel()
        self.current_dir = os.path.dirname(__file__)
        self.logo_dir = os.path.join(os.path.dirname(self.current_dir), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)

        # Set up the font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.setup_logo()
        self.setup_topbar()
        self.setup_bottom()
        self.setup_button()
        self.setup_widget()

    def setup_logo(self):
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(60, 60, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

    def setup_topbar(self):
        self.top_frame.setMaximumHeight(100)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.top_frame.setStyleSheet("background:white;")
        self.top_frame_layout.addWidget(self.logo)
        self.top_frame_layout.addStretch()
        self.top_frame_layout.addWidget(self.customer_button)
        
    def setup_bottom(self):
        self.customer_button.setFixedWidth(100)
        self.customer_button.setFixedHeight(40)
        self.customer_button.setFont(self.font)
        self.customer_button.setStyleSheet("color: white; background: #efbe25; border-radius: 5px;")


    def setup_button(self):
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

    def setup_widget(self):
        self.admin_layout.setContentsMargins(0, 0, 0, 0)
        self.admin_layout.setSpacing(0)
        self.admin_layout.addWidget(self.top_frame)
        self.admin_layout.addWidget(self.bottom_frame)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = admin_window()
    window.show()
    sys.exit(app.exec_())
