import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ..api import api
from ..config.carTileScroll import carTile_scroll
from ..config.font import font
from ..currentUser import CurrentUser
from .carTile import car_tile
from .reservationHistory import reservations_history
from .searchBar import search_bar
from .sideBar import side_bar
from .test import searchCar


class customer_window(QWidget):
    """
    A class to make the customer side of the application where you can search for cars to rent and make the reservations.
    """

    def __init__(self):
        """
        Initializes the customer window class.
        """
        super().__init__()
        # setup api call obj
        self.api = api()

        # setup customer window layout
        self.main_layout = QHBoxLayout(self)
        self.sub_window = QFrame()
        # self.sub_window.setStyleSheet("border: none; background-color: white;")
        self.customer_layout = QVBoxLayout(self.sub_window)
        self.main_layout.setContentsMargins(
            0, 0, 0, 0
        )  # Left, Top, Right, Bottom margins
        self.main_layout.setSpacing(0)  # Spacing between widgets
        self.customer_layout.setContentsMargins(
            0, 0, 0, 0
        )  # Left, Top, Right, Bottom margins
        self.customer_layout.setSpacing(0)  # Spacing between widgets

        # setup sidebar
        self.side_bar = side_bar()
        self.side_bar.menu_button.clicked.connect(self.menu_clicked)
        self.side_bar.h_home_button.clicked.connect(self.home_clicked)
        self.side_bar.s_home_button.clicked.connect(self.home_clicked)
        self.side_bar.h_table_button.clicked.connect(self.table_clicked)
        self.side_bar.s_table_button.clicked.connect(self.table_clicked)

        # setup Qframes
        self.top_frame = QFrame()
        self.top_frame_layout = QHBoxLayout(self.top_frame)

        # set up scrollable bottom frame
        self.bottom_frame = QFrame()
        self.scroll_area = carTile_scroll()
        self.reservations_history = reservations_history()

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
        self.signout_button = QPushButton("Sign Out")

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        # setup carlist and tile list
        self.list = []
        self.carList = []

        self.setup_topframe()
        self.setup_bottomframe()
        self.setup_tiles()
        self.setup_button()
        self.setup_widget()

    def setup_topframe(self):
        """
        function to setup the parameter for the top frame of the customer window that has the sign out button and the logo.
        """
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFixedHeight(75)
        self.top_frame.setStyleSheet("background: white;")
        self.top_frame_layout.addWidget(self.side_bar.menu_button)
        self.top_frame_layout.addStretch()

    def setup_button(self):
        """
        function to set up the parameters for the sign out button.
        """
        self.signout_button.setFixedWidth(100)
        self.signout_button.setFixedHeight(40)
        self.signout_button.setFont(self.font)
        self.signout_button.setStyleSheet(
            "color: white; background-color: #efbe25; border-radius: 5px; outline: none;"
        )

    def setup_bottomframe(self):
        """
        function to set up the parameters for the bottom frame and add the widget for the inital search window and the window that shows all the car tiles.
        """
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.bottom_layout = QStackedLayout(self.bottom_frame)
        self.bottom_layout.addWidget(self.search_bar)
        self.bottom_layout.addWidget(self.tile_widget)
        self.bottom_layout.addWidget(self.reservations_history)
        self.bottom_layout.setCurrentIndex(0)

    def setup_tiles(self):
        """
        function to setup the window that shows the search bar and car tiles after the inital search.
        """
        self.tile_search = search_bar()
        self.tile_layout.addWidget(self.tile_search, alignment=Qt.AlignCenter)
        self.tile_layout.addWidget(self.scroll_area)
        self.tile_search.search_button.clicked.connect(self.click_research)

    def setup_widget(self):
        """
        function to set up the layout of the customer window.
        """
        self.customer_layout.setContentsMargins(0, 0, 0, 0)
        self.customer_layout.setSpacing(0)
        self.top_frame_layout.addWidget(self.signout_button)
        self.customer_layout.addWidget(self.top_frame)
        self.customer_layout.addWidget(self.bottom_frame)
        self.main_layout.addWidget(self.side_bar)
        self.main_layout.addWidget(self.sub_window)

    def click_search(self):
        """
        function that when inital search is clicked it calls backend api to get a list of abvilable cars and displays them.
        """
        self.bottom_layout.setCurrentIndex(1)
        start_date = self.search.date_range.start_date_edit.date()
        end_date = self.search.date_range.end_date_edit.date()
        num_days = start_date.daysTo(end_date)
        self.list.clear()
        self.carList.clear()
        print(
            start_date.toString("yyyy-MM-dd")
            + " "
            + end_date.toString("yyyy-MM-dd")
            + " "
            + self.search.type_box.currentText()
        )
        self.carList = self.api.car_rental_obj.customer_search(
            start_date.toString("yyyy-MM-dd"),
            end_date.toString("yyyy-MM-dd"),
            self.search.type_box.currentText(),
        )
        self.clear_layout(self.scroll_area.scroll_frameLayout)

        for i in range(len(self.carList)):
            self.list.append(
                car_tile(self.carList[i], self, num_days, start_date, end_date)
            )
            self.scroll_area.scroll_frameLayout.addWidget(
                self.list[i], alignment=Qt.AlignCenter
            )

    def click_research(self):
        """
        function that when serach is clicked after the inital search call the backend api to get a new list of cars to display.
        """
        self.bottom_layout.setCurrentIndex(1)
        start_date = self.tile_search.date_range.start_date_edit.date()
        end_date = self.tile_search.date_range.end_date_edit.date()
        num_days = start_date.daysTo(end_date)
        self.list.clear()
        self.carList.clear()
        self.carList = self.api.car_rental_obj.customer_search(
            start_date.toString("yyyy-MM-dd"),
            end_date.toString("yyyy-MM-dd"),
            self.tile_search.type_box.currentText(),
        )
        print(
            start_date.toString("yyyy-MM-dd")
            + " "
            + end_date.toString("yyyy-MM-dd")
            + " "
            + self.tile_search.type_box.currentText()
        )
        self.clear_layout(self.scroll_area.scroll_frameLayout)

        for i in range(len(self.carList)):
            self.list.append(
                car_tile(self.carList[i], self, num_days, start_date, end_date)
            )
            self.scroll_area.scroll_frameLayout.addWidget(
                self.list[i], alignment=Qt.AlignCenter
            )

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

    def menu_clicked(self):
        if self.side_bar.hiden_bar.isHidden() is True:
            self.side_bar.hiden_bar.show()
            self.side_bar.shown_bar.hide()
        else:
            self.side_bar.hiden_bar.hide()
            self.side_bar.shown_bar.show()

    def table_clicked(self):
        currentUser = CurrentUser()
        user = currentUser.get_user()
        self.bottom_layout.setCurrentIndex(2)
        self.reservations_history.setup_table(user.cust_id, user.user)

    def home_clicked(self):
        self.bottom_layout.setCurrentIndex(0)


if __name__ == "__main__":
    import sys

    from ..config.screenConfig import screen_config

    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = customer_window()
    window.show()
    sys.exit(app.exec_())
