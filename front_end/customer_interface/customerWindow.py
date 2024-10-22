import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from .carTile import car_tile
from .searchBar import search_bar


class customer_window(QWidget):
    def __init__(self):
        super().__init__()
        # setup customer window layout
        self.customer_layout = QVBoxLayout(self)

        # setup Qframes
        self.top_frame = QFrame(self)
        self.top_frame_layout = QHBoxLayout(self.top_frame)

        #set up scrollable bottom frame
        self.bottom_frame = QFrame(self)
        self.scroll_area = QScrollArea(self)

        # setup search bar
        self.search_bar = QWidget()
        self.search_layout = QHBoxLayout(self.search_bar)
        self.search = search_bar()
        self.search_layout.addWidget(self.search, alignment=Qt.AlignCenter)

        # setup tile window
        self.tile_window = QFrame(self)

        # setup sub widgets
        self.admin_button = QPushButton("Admin",self.top_frame)

        # setup logo
        self.logo = QLabel(self)
        self.current_dir = os.path.dirname(__file__)
        self.logo_dir = os.path.join(os.path.dirname(self.current_dir), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.setup_logo()
        self.setup_topframe()
        self.setup_bottomframe()
        self.setup_tiles()
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
        self.bottom_layout = QStackedLayout(self.bottom_frame)
        self.bottom_layout.addWidget(self.search_bar)
        self.bottom_layout.addWidget(self.scroll_area)
        self.bottom_layout.setCurrentIndex(1)


    def setup_tiles(self):
        self.tile_layout = QVBoxLayout(self.tile_window)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.tile_window)
        self.scroll_area.setStyleSheet("""
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 8px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #bfbfbf;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #999999;
            }
            QScrollBar::handle:vertical:pressed {
                background-color: #787878;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 8px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background-color: #bfbfbf;
                min-width: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:horizontal:hover {
                background-color: #999999;
            }
            QScrollBar::handle:horizontal:pressed {
                background-color: #787878;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
        """)
        self.list = []
        
        for i in range(9):
            self.list.append(car_tile())
            self.tile_layout.addWidget(self.list[i], alignment=Qt.AlignCenter) 



 
    def setup_widget(self):
        self.customer_layout.setContentsMargins(0, 0, 0, 0)
        self.customer_layout.setSpacing(0)
        self.top_frame_layout.addWidget(self.admin_button)
        self.customer_layout.addWidget(self.top_frame)
        self.customer_layout.addWidget(self.bottom_frame)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = customer_window()
    window.show()
    sys.exit(app.exec_())
