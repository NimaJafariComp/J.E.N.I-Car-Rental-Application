from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from font import font


class customer_window(QWidget):
    def __init__(self):
        super().__init__()
        self.customer_layout = QVBoxLayout(self)
        self.customer_layout.setContentsMargins(0, 0, 0, 0)
        self.customer_layout.setSpacing(0)

        #set up logo img
        self.logo = QLabel(self)
        self.pixmap = QPixmap("logo/FullLogo.png")
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(120, 120, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

        # Set up the font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)
        self.font.setBold(True)


        self.top_frame = QWidget(self)
        self.top_frame.setFixedHeight(150)
        self.top_frame.setStyleSheet(
            "background: lightgrey;"
        )

        self.top_frame_layout = QHBoxLayout(self.top_frame)
        self.top_frame_layout.addWidget(self.logo)
        self.top_frame_layout.addStretch()
        self.admin_button = QPushButton("Admin",self.top_frame)
        self.top_frame_layout.addWidget(self.admin_button)
        self.admin_button.setFixedWidth(200)
        self.admin_button.setFixedHeight(75)
        self.admin_button.setStyleSheet(
            "background-color: white;"
            "border: 3px soild black;"
            "border-radius: 5px;"
        )

        self.customer_layout.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self)
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
    
        self.customer_layout.addWidget(self.bottom_frame)
