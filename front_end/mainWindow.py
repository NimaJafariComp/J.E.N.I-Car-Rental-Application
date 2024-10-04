import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from customerWindow import customer_window
from adminWindow import admin_window
from login import login


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1155, 912)
        self.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.setGeometry(0, 0, 1920, 1080)

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")


        self.stacked_widget = QStackedLayout(self.central_widget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setSpacing(0)
        self.stacked_widget.setContentsMargins(0, 0, 0, 0)       

        self.setCentralWidget(self.central_widget)

        self.c_window = customer_window()
        self.a_window = admin_window()
        self.log_window = login()
        self.stacked_widget.addWidget(self.c_window)
        self.stacked_widget.addWidget(self.a_window)
        self.stacked_widget.addWidget(self.log_window)
        self.stacked_widget.setCurrentIndex(0) 

        self.c_window.admin_button.clicked.connect(self.on_click_admin)
        self.a_window.customer_button.clicked.connect(self.on_click_customer)

        self.center()


    def on_click_admin(self):
        self.stacked_widget.setCurrentIndex(2)
        self.log_window.login_button.clicked.connect(self.switch_to_admin)

    def switch_to_admin(self):
        self.pw = "password"
        self.entered_pw = self.log_window.pw_box.text()
        if self.pw == self.entered_pw: 
            self.stacked_widget.setCurrentIndex(1)
            self.log_window.pw_box.clear()

    def on_click_customer(self):
        self.stacked_widget.setCurrentIndex(0)

    # Method to center the window on the screen
    def center(self):
        # Get the rectangle of the screen where the application is being displayed
        qr = self.frameGeometry()
        
        # Get the center point of the screen
        cp = QDesktopWidget().availableGeometry().center()
        
        # Move the rectangle's center point to the center of the screen
        qr.moveCenter(cp)
        
        # Move the top-left of the window to the top-left of the rectangle
        self.move(qr.topLeft())


if __name__ == "__main__":
    import sys
    from screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
