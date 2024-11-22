from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class transition(QWidget):
    '''
    A class to make a widget that allows you to go back to the selection window.
    '''
    def __init__(self, admin_window, central_widget, center):
        '''
        Initilizes class.
        '''
        super().__init__()

        # Main Layout for the Widget
        self.main_layout = QVBoxLayout(self)
        self.admin_window = admin_window
        self.central_widget = central_widget
        self.center = center

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.setup_bottom()
        self.setup_central()
        self.setup_main()

    def setup_bottom(self):
        '''
        function to set up the bottom frame that that hold the back button.
        '''
        self.bottom_frame = QFrame()
        self.bottom_frame.setFixedHeight(75)
        self.bottom_layout = QHBoxLayout(self.bottom_frame)
        self.back_button = QPushButton('Back')
        self.back_button.setFixedSize(100,50)
        self.back_button.setFont(self.font)
        self.back_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.back_button.clicked.connect(self.clicked_back)
        self.bottom_layout.addStretch()
        self.bottom_layout.addWidget(self.back_button)

    def setup_central(self):
        '''
        function to set up the main window that will have the widget to be used.
        '''
        self.central = QFrame()

        self.central.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.central_layout = QVBoxLayout(self.central)
        if self.center == 1:
            self.central_layout.addWidget(self.central_widget, alignment=Qt.AlignCenter)
        else:
            self.central_layout.addWidget(self.central_widget)

    def setup_main(self):
        '''
        function to setup main layout
        '''
        self.main_layout.addWidget(self.central)
        self.main_layout.addWidget(self.bottom_frame)

    def clicked_back(self):
        '''
        function to go back to previous window when back button is clicked.
        '''
        self.admin_window.bottom_layout.setCurrentIndex(0)



if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    label = QLabel("dude")
    center_window = QWidget()
    center_layout = QStackedLayout(center_window)
    sys.exit(app.exec_())


