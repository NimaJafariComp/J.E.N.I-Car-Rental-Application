import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .customer_interface.customerWindow import customer_window
from .admin_interface.adminWindow import admin_window
from .login import login
from .adminLogin import admin_login
from .customerLogin import customer_login
from .customerSignup import customer_signup
from .adminSignup import admin_signup
from .currentUser import CurrentUser    

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
        self.log_window = login(self)
        self.admin_login = admin_login(self) 
        self.customer_login = customer_login(self)
        self.admin_signup = admin_signup(self)
        self.customer_signup = customer_signup(self)
        self.c_window = customer_window()
        self.a_window = admin_window()

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

        self.stacked_widget.addWidget(self.log_window)
        self.stacked_widget.addWidget(self.customer_login)
        self.stacked_widget.addWidget(self.admin_login)
        self.stacked_widget.addWidget(self.customer_signup)
        self.stacked_widget.addWidget(self.admin_signup)
        self.stacked_widget.addWidget(self.c_window)
        self.stacked_widget.addWidget(self.a_window)
        self.stacked_widget.setCurrentIndex(0) 

        self.c_window.signout_button.clicked.connect(self.click_signout)
        self.a_window.signout_button.clicked.connect(self.click_signout)

    def click_signout(self):
        '''
        funtion to set up the login button.
        '''
        currentUser = CurrentUser()
        currentUser.set_user(None)
        print(currentUser.get_user())

        self.stacked_widget.setCurrentIndex(0)

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
