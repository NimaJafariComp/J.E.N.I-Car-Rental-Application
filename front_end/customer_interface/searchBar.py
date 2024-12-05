from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ..config.font import font


class search_bar(QWidget):
    """
    A class that makes a search widget to search the data base for a list of cars from a spescific date range and type.
    """

    def __init__(self):
        """
        initializes the search bar class on make.
        """
        super().__init__()
        # setup main layout
        self.main_layout = QHBoxLayout(self)
        self.setFixedSize(800, 100)

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        # setup start and end date boxes
        self.date_range = date_picker()

        # setup the type box
        self.type_box = QComboBox()

        # setup search button
        self.search_button = QPushButton("Search")

        # call setup for the widget
        self.setup_search()

    def setup_button(self):
        """
        function to set the parameters for the search button.
        """
        self.search_button.setFixedWidth(100)
        self.search_button.setFixedHeight(30)
        self.search_button.setFont(self.font)
        self.search_button.setStyleSheet(
            "color: white; background:#efbe25; border-radius: 5px; outline: none;"
        )

    def setup_typebox(self):
        """
        function to set up the parameters for type combo box.
        """
        self.type_box.addItems(["Sedan", "Truck", "Coupe", "SUV"])

    def setup_search(self):
        """
        function to call all setup functions and add widgets to layout.
        """
        self.setup_button()
        self.setup_typebox()

        self.main_layout.addWidget(self.date_range)
        self.main_layout.addWidget(self.type_box)
        self.main_layout.addWidget(self.search_button)


class date_picker(QWidget):
    """
    A class to make the dropdown calendar to pick the dates.
    """

    def __init__(self):
        super().__init__()
        # Set up the layout
        layout = QHBoxLayout()

        # Start Date QDateEdit
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)  # Enable dropdown calendar
        self.start_date_edit.setDate(QDate.currentDate())
        self.start_date_edit.dateChanged.connect(
            self.update_end_date_minimum
        )  # Connect to update function
        layout.addWidget(self.start_date_edit)

        # End Date QDateEdit
        self.end_date_edit = QDateEdit(self)
        self.end_date_edit.setCalendarPopup(True)  # Enable dropdown calendar
        self.end_date_edit.setDate(QDate.currentDate())
        layout.addWidget(self.end_date_edit)

        # Set initial minimum date for end date
        self.update_end_date_minimum()

        # Set layout
        self.setLayout(layout)

    def update_end_date_minimum(self):
        """
        Update the minimum date of the end date selector.
        """
        start_date = self.start_date_edit.date()
        self.end_date_edit.setMinimumDate(start_date)


if __name__ == "__main__":
    import sys

    from ..config.screenConfig import screen_config

    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = search_bar()
    window.show()
    sys.exit(app.exec_())
