import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .config.font import font

class login(QWidget):
    def __init__(self):
        super().__init__()
        # Set the background color of the main window to dark grey

        # Set up the main layout and inner login window
        self.login_layout = QVBoxLayout(self)
        self.login_window = QWidget()
        self.login_window_layout = QVBoxLayout(self.login_window)

        #set up logo img
        self.logo = QLabel()
        self.logo_dir = os.path.join(os.path.dirname(__file__), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)


        # Set up the font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)
        #self.font.setBold(True)

        # Create label and set font
        self.admin_label = QLabel("ADMIN")

        # Password box
        self.pw_box = QLineEdit()
        
        # Login button
        self.login_button = QPushButton("Login")

        # function calls
        self.setup_layout()
        self.setup_logo()
        self.setup_admin_label()
        self.setup_pw_box()
        self.setup_login_button() 

    def setup_logo(self):
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(300, 300, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

    def setup_layout(self):
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
        self.login_window_layout.addWidget(self.pw_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        self.login_window_layout.addStretch()

        # Add the login window to the main layout, centering it
        self.login_layout.addWidget(self.login_window, alignment=Qt.AlignCenter)



    def setup_admin_label(self):
        self.admin_label.setFont(self.font)
        self.admin_label.setStyleSheet("color: #efbe25; border: none;")

    def setup_pw_box(self):
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
        self.login_button.setFont(self.font)
        self.login_button.setFixedWidth(125)
        self.login_button.setFixedHeight(40)
        self.login_button.setStyleSheet(
            "background-color: #efbe25; color: white;"
            "border: none;"
            "border-radius : 5px;"
        )

if __name__ == "__main__":
    import sys
    from .config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = login()
    window.show()
    sys.exit(app.exec_())
