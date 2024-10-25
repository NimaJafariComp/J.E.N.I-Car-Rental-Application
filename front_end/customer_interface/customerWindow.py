import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from .carTile import car_tile
from .searchBar import search_bar
from .test import searchCar


class customer_window(QWidget):
    def __init__(self):
        super().__init__()
        # setup customer window layout
        self.customer_layout = QVBoxLayout(self)

        # setup Qframes
        self.top_frame = QFrame()
        self.top_frame_layout = QHBoxLayout(self.top_frame)

        #set up scrollable bottom frame
        self.bottom_frame = QFrame()
        self.scroll_area = QScrollArea()

        # setup tile layout
        self.tile_widget = QFrame()
        self.tile_layout = QVBoxLayout(self.tile_widget)

        # setup search bar
        self.search_bar = QWidget()
        self.search_layout = QHBoxLayout(self.search_bar)
        self.search = search_bar()
        self.search_layout.addWidget(self.search, alignment=Qt.AlignCenter)
        self.search.search_button.clicked.connect(self.click_search)

        # setup tile window
        self.tile_window = QFrame()
        self.scroll_layout = QVBoxLayout(self.tile_window)

        # setup sub widgets
        self.admin_button = QPushButton("Admin")

        # setup logo
        self.logo = QLabel()
        self.current_dir = os.path.dirname(__file__)
        self.logo_dir = os.path.join(os.path.dirname(self.current_dir), "logo/HalfLogo.png")
        self.pixmap = QPixmap(self.logo_dir)

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        # setup carlist and tile list
        self.list = []
        self.carList = []

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
        self.bottom_layout.addWidget(self.tile_widget)
        self.bottom_layout.setCurrentIndex(0)

    def setup_tiles(self):
        self.tile_search = search_bar()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.tile_window)
        self.tile_layout.addWidget(self.tile_search, alignment=Qt.AlignCenter)
        self.tile_layout.addWidget(self.scroll_area)
        self.tile_search.search_button.clicked.connect(self.click_research)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }
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
 
    def setup_widget(self):
        self.customer_layout.setContentsMargins(0, 0, 0, 0)
        self.customer_layout.setSpacing(0)
        self.top_frame_layout.addWidget(self.admin_button)
        self.customer_layout.addWidget(self.top_frame)
        self.customer_layout.addWidget(self.bottom_frame)

    def click_search(self):
        self.bottom_layout.setCurrentIndex(1)
        self.carList = searchCar()
        
        for i in range(len(self.carList)):
            self.list.append(car_tile(self.carList[i]))
            self.scroll_layout.addWidget(self.list[i], alignment=Qt.AlignCenter) 

    def click_research(self):
        self.bottom_layout.setCurrentIndex(1)
        self.list.clear()
        self.carList.clear()
        self.carList = searchCar()
        self.clear_layout(self.scroll_layout)
        
        for i in range(len(self.carList)-2):
            self.list.append(car_tile(self.carList[i]))
            self.scroll_layout.addWidget(self.list[i], alignment=Qt.AlignCenter) 
 
    def clear_layout(self, layout):
        """
        Remove all widgets from a given layout.
        """
        while layout.count() > 0:
            # Get the widget at index 0
            item = layout.takeAt(0)

            # If the item is a widget, delete it
            if item.widget():
                item.widget().deleteLater()




if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = customer_window()
    window.show()
    sys.exit(app.exec_())
