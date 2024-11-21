import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .customer_interface.customerWindow import customer_window
from .admin_interface.adminWindow import admin_window
from .login import login

class main_window(QMainWindow):
    '''
    Class to make the main window for the application.
    '''
    def __init__(self):
        '''
        Initializes all the code to make the main window.
        '''
        super().__init__()
        self.central_widget = QWidget()
        self.stacked_widget = QStackedLayout(self.central_widget)
        self.c_window = customer_window()
        self.a_window = admin_window()
        self.log_window = login()

        self.center()
        self.setup_mainwindow()
        self.manage_stack()

    def setup_mainwindow(self):
        '''
        function to set up the main windows perameters.
        '''
        self.setContentsMargins(0, 0, 0, 0)
        self.resize(1155, 912)
        self.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.setGeometry(0, 0, 1920, 1080)

    def manage_stack(self):
        '''
        function to manage the main stacked widget of the application.
        '''
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)
        
        self.stacked_widget.setObjectName("stacked_widget")
        self.stacked_widget.setSpacing(0)
        self.stacked_widget.setContentsMargins(0, 0, 0, 0)       

        self.stacked_widget.addWidget(self.c_window)
        self.stacked_widget.addWidget(self.a_window)
        self.stacked_widget.addWidget(self.log_window)
        self.stacked_widget.setCurrentIndex(0) 

        self.c_window.admin_button.clicked.connect(self.on_click_admin)
        self.a_window.customer_button.clicked.connect(self.on_click_customer)

    def on_click_admin(self):
        '''
        funtion to set up the login button.
        '''
        self.stacked_widget.setCurrentIndex(2)
        self.log_window.login_button.clicked.connect(self.switch_to_admin)
        self.log_window.pw_box.returnPressed.connect(self.switch_to_admin)
        self.log_window.back_button.clicked.connect(self.login_back)

    def switch_to_admin(self):
        '''
        funtion to check login information and login to admin side when login button in login window is pressed.
        '''
        self.user = "admin"
        self.pw = "password"
        self.entered_user = self.log_window.user_box.text()
        self.entered_pw = self.log_window.pw_box.text()

        if self.pw == self.entered_pw and self.user == self.entered_user: 
            self.stacked_widget.setCurrentIndex(1)
            self.a_window.bottom_layout.setCurrentIndex(0)
            self.log_window.pw_box.clear()

    def on_click_customer(self):
        '''
        funtion to go to customer window when customer button is clicked.
        '''
        self.stacked_widget.setCurrentIndex(0)
        
    def login_back(self):
        '''
        funtion to go back to customer window when in login screen and pressed back button.
        '''
        self.stacked_widget.setCurrentIndex(0)

    # Method to center the window on the screen
    def center(self):
        '''
        funtion to center the application in the screen.
        '''
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
    from .config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
