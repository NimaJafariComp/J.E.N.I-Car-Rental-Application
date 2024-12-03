import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .api import api
from .config.font import font
from .currentUser import CurrentUser


class admin_login(QWidget):
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
        self.api = api()
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
        self.admin_label = QLabel("Admin Login")
        self.wrong_login = QLabel("Passwords or Username incorrect try again.")
        self.wrong_login.setStyleSheet("border : none; color : red;")
        self.wrong_login.hide()

        # username box
        self.user_box = QLineEdit()

        # Password box
        self.pw_box = QLineEdit()

        # Login button
        self.buttons = QFrame()
        self.buttons_layout = QHBoxLayout(self.buttons)
        self.login_button = QPushButton("Login")
        self.back_button = QPushButton("Back")
        self.buttons.setStyleSheet("border: none;")

        # setup clickable sign up label
        self.signup_label = QLabel('<a href="https://example.com">Sign Up Here</a>')
        self.signup_label.setOpenExternalLinks(
            False
        )  # Disable opening the link in a browser
        self.signup_label.linkActivated.connect(
            self.on_label_click
        )  # Connect to your custom function
        self.signup_label.setStyleSheet("border : none;")
        self.signup_label.setCursor(Qt.PointingHandCursor)

        # function calls
        self.setup_layout()
        self.setup_logo()
        self.setup_admin_label()
        self.setup_user_box()
        self.setup_pw_box()
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
        self.login_window_layout.addWidget(self.admin_label, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.wrong_login, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.user_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.pw_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.buttons, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.signup_label, alignment=Qt.AlignCenter)
        self.login_window_layout.addStretch()

        # Add the login window to the main layout, centering it
        self.login_layout.addWidget(self.login_window, alignment=Qt.AlignCenter)

    def setup_admin_label(self):
        """
        funtion to set up the parameters for the admin label.
        """
        self.admin_label.setFont(self.font)
        self.admin_label.setStyleSheet("color: #efbe25; border: none;")

    def setup_user_box(self):
        """
        function to set the parameters for the user name text box.
        """
        self.user_box.setPlaceholderText("Enter Username")
        self.user_box.setFixedWidth(300)
        self.user_box.setFixedHeight(40)
        self.user_box.setStyleSheet(
            "background-color:white;"
            "border : 1px solid lightgrey;"
            "border-radius : 5px;"
        )

    def setup_pw_box(self):
        """
        function to set up the parameters for the Password text box.
        """
        self.pw_box.setPlaceholderText("Enter Password")
        self.pw_box.setFixedWidth(300)
        self.pw_box.setFixedHeight(40)
        self.pw_box.setEchoMode(QLineEdit.Password)
        self.pw_box.setStyleSheet(
            "background-color:white;"
            "border : 1px solid lightgrey;"
            "border-radius : 5px;"
        )

    def setup_login_button(self):
        """
        function to set up the parameters for the login button.
        """
        self.login_button.setFont(self.font)
        self.back_button.setFont(self.font)
        self.login_button.setFixedWidth(125)
        self.login_button.setFixedHeight(40)
        self.back_button.setFixedWidth(125)
        self.back_button.setFixedHeight(40)
        self.login_button.setStyleSheet(
            "background-color: #efbe25; color: white;"
            "border: none;"
            "border-radius : 5px;"
        )
        self.back_button.setStyleSheet(
            "background-color: #efbe25; color: white;"
            "border: none;"
            "border-radius : 5px;"
        )
        self.buttons_layout.addWidget(self.back_button)
        self.buttons_layout.addWidget(self.login_button)
        self.login_button.clicked.connect(self.click_login)
        self.back_button.clicked.connect(self.click_back)
        self.pw_box.returnPressed.connect(self.click_login)
        self.user_box.returnPressed.connect(self.click_login)

    def click_login(self):
        """
        funtion to check login information and login to admin side when login button in login window is pressed.
        """
        user = "admin"
        pw = "password"
        entered_user = self.user_box.text()
        entered_pw = self.pw_box.text()
        user = self.api.car_rental_obj.user_login(entered_user, entered_pw, "admin")
        currentUser = CurrentUser()
        currentUser.set_user(user)

        if user is not None:
            self.main_window.stacked_widget.setCurrentIndex(6)
            self.main_window.a_window.bottom_layout.setCurrentIndex(0)
            self.user_box.clear()
            self.pw_box.clear()
        else:
            self.wrong_login.show()

    def on_label_click(self):
        self.main_window.stacked_widget.setCurrentIndex(4)

    def click_back(self):
        self.main_window.stacked_widget.setCurrentIndex(0)
        self.user_box.clear()
        self.pw_box.clear()
