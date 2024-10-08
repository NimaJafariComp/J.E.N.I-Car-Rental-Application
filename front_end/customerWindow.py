from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from font import font


class customer_window(QWidget):
    def __init__(self):
        super().__init__()
        # setup customer window layout
        self.customer_layout = QVBoxLayout(self)

        # setup Qframes
        self.top_frame = QFrame(self)
        self.top_frame_layout = QHBoxLayout(self.top_frame)
        self.bottom_frame = QFrame(self)

        # setup sub widgets
        self.admin_button = QPushButton("Admin",self.top_frame)

        # setup logo
        self.logo = QLabel(self)
        self.pixmap = QPixmap("logo/HalfLogo.png")

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.setup_logo()
        self.setup_topframe()
        self.setup_bottomframe()
        self.setup_button()
        self.setup_widget()

    def setup_logo(self):#set up logo img
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(60, 60, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

    def setup_topframe(self):
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFixedHeight(int(100))
        self.top_frame.setStyleSheet("background: white;")
        self.top_frame_layout.addWidget(self.logo)
        self.top_frame_layout.addStretch()

    def setup_button(self):
        self.admin_button.setFixedWidth(100)
        self.admin_button.setFixedHeight(40)
        self.admin_button.setFont(self.font)
        self.admin_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")

    def setup_bottomframe(self):
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
 
    def setup_widget(self):
        self.customer_layout.setContentsMargins(0, 0, 0, 0)
        self.customer_layout.setSpacing(0)
        self.top_frame_layout.addWidget(self.admin_button)
        self.customer_layout.addWidget(self.top_frame)
        self.customer_layout.addWidget(self.bottom_frame)

if __name__ == "__main__":
    import sys
    from screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = customer_window()
    window.show()
    sys.exit(app.exec_())
