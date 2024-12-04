import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .api import api
from .config.font import font


class customer_signup(QWidget):
    """
    Widget to make the login window.
    """

    def __init__(self, main_window):
        """
        Initializes the login window.
        """
        super().__init__()
        self.main_window = main_window
        self.api = api()

        # Set up the main layout and inner login window
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
        self.label_style = (
            "background-color:white; border : 1px solid lightgrey; border-radius : 5px;"
        )
        self.admin_label = QLabel("Customer Sign Up")
        self.pw_not_same = QLabel("Passwords do not match try again.")
        self.pw_not_same.setStyleSheet("border : none; color : red;")
        self.pw_not_same.hide()
        self.first_name_box = QLineEdit()
        self.last_name_box = QLineEdit()
        self.user_box = QLineEdit()
        self.email = QLineEdit()
        self.pw_box = QLineEdit()
        self.pw_confirm_box = QLineEdit()

        # Login button
        self.buttons = QFrame()
        self.buttons_layout = QHBoxLayout(self.buttons)
        self.login_button = QPushButton("Sign Up")
        self.back_button = QPushButton("Back")
        self.button_style = "background-color: #efbe25; color: white; border: none; border-radius : 5px; outline: none;"
        self.buttons.setStyleSheet("border: none;")

        # function calls
        self.setup_layout()
        self.setup_logo()
        self.setup_admin_label()
        self.text_box()
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
        self.login_window.setFixedHeight(800)

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
        self.login_window_layout.addWidget(self.admin_label, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.pw_not_same, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(
            self.first_name_box, alignment=Qt.AlignCenter
        )
        self.login_window_layout.addWidget(self.last_name_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.user_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.email, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.pw_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(
            self.pw_confirm_box, alignment=Qt.AlignCenter
        )
        self.login_window_layout.addWidget(self.buttons, alignment=Qt.AlignCenter)
        self.login_window_layout.addStretch()

        # Add the login window to the main layout, centering it
        self.login_layout.addWidget(self.login_window, alignment=Qt.AlignCenter)

    def setup_admin_label(self):
        """
        funtion to set up the parameters for the admin label.
        """
        self.admin_label.setFont(self.font)
        self.admin_label.setStyleSheet("color: #efbe25; border: none;")

    def text_box(self):
        """
        function to set the parameters for the user name text box.
        """
        self.first_name_box.setPlaceholderText("First Name")
        self.first_name_box.setFixedWidth(300)
        self.first_name_box.setFixedHeight(40)
        self.first_name_box.setStyleSheet(self.label_style)

        self.last_name_box.setPlaceholderText("Last Name")
        self.last_name_box.setFixedWidth(300)
        self.last_name_box.setFixedHeight(40)
        self.last_name_box.setStyleSheet(self.label_style)

        self.email.setPlaceholderText("Email")
        self.email.setFixedWidth(300)
        self.email.setFixedHeight(40)
        self.email.setStyleSheet(self.label_style)

        self.user_box.setPlaceholderText("Enter Username")
        self.user_box.setFixedWidth(300)
        self.user_box.setFixedHeight(40)
        self.user_box.setStyleSheet(self.label_style)

        self.pw_box.setPlaceholderText("Enter Password")
        self.pw_box.setFixedWidth(300)
        self.pw_box.setFixedHeight(40)
        self.pw_box.setEchoMode(QLineEdit.Password)
        self.pw_box.setStyleSheet(self.label_style)

        self.pw_confirm_box.setPlaceholderText("Re-Enter Password")
        self.pw_confirm_box.setFixedWidth(300)
        self.pw_confirm_box.setFixedHeight(40)
        self.pw_confirm_box.setEchoMode(QLineEdit.Password)
        self.pw_confirm_box.setStyleSheet(self.label_style)

    def setup_login_button(self):
        """
        function to set up the parameters for the login button.
        """
        self.login_button.setFont(self.font)
        self.login_button.setFixedWidth(125)
        self.login_button.setFixedHeight(40)
        self.login_button.setStyleSheet(self.button_style)

        self.back_button.setFont(self.font)
        self.back_button.setFixedWidth(125)
        self.back_button.setFixedHeight(40)
        self.back_button.setStyleSheet(self.button_style)

        self.buttons_layout.addWidget(self.back_button)
        self.buttons_layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.click_signup)
        self.back_button.clicked.connect(self.click_back)

    def click_signup(self):
        """
        funtion to check login information and login to admin side when login button in login window is pressed.
        """
        if self.pw_box.text() == self.pw_confirm_box.text():
            name = self.first_name_box.text() + " " + self.last_name_box.text()
            username = self.user_box.text()
            email = self.email.text()
            pw = self.pw_box.text()
            dob = "01/01/1900"
            self.api.car_rental_obj.user_signup(
                name, username, email, pw, dob, "customer"
            )
            self.main_window.stacked_widget.setCurrentIndex(0)
        else:
            self.pw_not_same.show()
            return

        self.pw_box.clear()
        self.pw_confirm_box.clear()

    def click_back(self):
        self.main_window.stacked_widget.setCurrentIndex(1)
