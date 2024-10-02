from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class login(QWidget):
    def __init__(self):
        super().__init__()

        self.valid = 0

        self.login_layout = QVBoxLayout(self)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(0)

        self.login_window = QWidget(self)
        self.login_window.setFixedWidth(300)
        self.login_window.setFixedHeight(500)
        self.admin_label = QLabel("ADMIN", self)
        self.pw_box = QLineEdit(self)
        self.login_button = QPushButton("Login", self)
        self.pw_box.setStyleSheet(
            "background:white;"
            "border : 2px solid black;"
            "border-radius : 20px;"
        )
        self.login_button.setStyleSheet(
            "background:white;"
            "border : 2px solid black;"
            "border-radius : 20px;"
        )
        self.login_window.setStyleSheet(
            "background:grey;"
            "border-radius: 35px;"
        )
        self.login_window_layout = QVBoxLayout(self.login_window) 
        self.login_window_layout.addStretch()
        self.login_window_layout.addWidget(self.admin_label)
        self.login_window_layout.addWidget(self.pw_box)
        self.login_window_layout.addWidget(self.login_button)
        self.login_window_layout.addStretch()

        self.inside_frame = QFrame(self)
        self.inside_layout = QHBoxLayout(self.inside_frame)

        self.inside_layout.addStretch()
        self.inside_layout.addWidget(self.login_window)
        self.inside_layout.addStretch()

        
        self.login_layout.addStretch()
        self.login_layout.addWidget(self.inside_frame)
        self.login_layout.addStretch()


        




