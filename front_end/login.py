import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .adminLogin import admin_login
from .config.font import font


class login(QWidget):
    """
    Widget to make the login window.
    """

    def __init__(self, main_window):
        """
        Initializes the login window.
        """
        super().__init__()
        # Set the background color of the main window to dark grey

        # Set up the main layout and inner login window
        self.main_window = main_window
        self.login_layout = QVBoxLayout(self)
        self.login_window = QWidget()
        self.login_window_layout = QVBoxLayout(self.login_window)

        # set up logo img
        self.logo = QLabel()
        self.logo_dir = os.path.join(os.path.dirname(__file__), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)

        # Set up the font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)
        # self.font.setBold(True)

        # Create label and set font
        self.login_label = QLabel("Select Login")

        # Login button
        self.customer_login_button = QPushButton("Customer Login")
        self.admin_login_button = QPushButton("Admin Login")

        # function calls
        self.setup_layout()
        self.setup_logo()
        self.setup_admin_label()
        self.setup_login_button()

    def setup_logo(self):
        """
        function to set parameters for the image logo for the login window.
        """
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(
            300, 300, aspectRatioMode=1
        )  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

    def setup_layout(self):
        """
        function to setup the main layou for the login window.
        """
        self.setStyleSheet("background-color:darkgrey;")
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(0)

        # Create the inner login window
        self.login_window.setFixedWidth(400)
        self.login_window.setFixedHeight(600)

        # Style for the login window
        self.login_window.setStyleSheet(
            "background-color:white;"
            "border : 3px solid lightgrey;"
            "border-radius: 25px;"
        )

        # Layout for the inner login window
        self.login_window_layout.addStretch()
        self.login_window_layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        self.login_window_layout.addStretch()
        self.login_window_layout.addWidget(self.login_label, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(
            self.customer_login_button, alignment=Qt.AlignCenter
        )
        self.login_window_layout.addWidget(
            self.admin_login_button, alignment=Qt.AlignCenter
        )
        self.login_window_layout.addStretch()

        # Add the login window to the main layout, centering it
        self.login_layout.addWidget(self.login_window, alignment=Qt.AlignCenter)

    def setup_admin_label(self):
        """
        funtion to set up the parameters for the admin label.
        """
        self.login_label.setFont(self.font)
        self.login_label.setStyleSheet("color: #efbe25; border: none;")

    def setup_login_button(self):
        """
        function to set up the parameters for the login button.
        """
        self.customer_login_button.setFont(self.font)
        self.admin_login_button.setFont(self.font)
        self.customer_login_button.setFixedWidth(150)
        self.customer_login_button.setFixedHeight(40)
        self.admin_login_button.setFixedWidth(150)
        self.admin_login_button.setFixedHeight(40)
        self.customer_login_button.setStyleSheet(
            "background-color: #efbe25; color: white;"
            "border: none;"
            "border-radius : 5px; outline: none;"
        )
        self.admin_login_button.setStyleSheet(
            "background-color: #efbe25; color: white;"
            "border: none;"
            "border-radius : 5px; outline: none;"
        )
        self.admin_login_button.clicked.connect(self.click_admin_button)
        self.customer_login_button.clicked.connect(self.click_customer_button)

    def click_admin_button(self):
        self.main_window.stacked_widget.setCurrentIndex(2)

    def click_customer_button(self):
        self.main_window.stacked_widget.setCurrentIndex(1)


if __name__ == "__main__":
    import sys

    from .config.screenConfig import screen_config

    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = login()
    window.show()
    sys.exit(app.exec_())
