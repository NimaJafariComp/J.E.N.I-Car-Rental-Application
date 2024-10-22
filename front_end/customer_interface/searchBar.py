from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class search_bar(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout(self)
        self.setFixedSize(800, 100)

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.start_date = date_picker()
        self.end_date = date_picker()

        self.main_layout.addWidget(self.start_date)
        self.main_layout.addWidget(self.end_date)

        self.search_button = QPushButton("Search", self)
        self.setup_button()

        self.main_layout.addWidget(self.search_button)
    
    def setup_button(self):
        self.search_button.setFixedWidth(100)
        self.search_button.setFixedHeight(30)
        self.search_button.setFont(self.font)
        self.search_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")


class date_picker(QWidget):
    def __init__(self):
        super().__init__()
        # Set up the window layout
        self.date_layout = QVBoxLayout()

        # make a date variable 

        # Create a QDateEdit widget
        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)  # Enable the dropdown calendar
        self.date_edit.setDate(QDate.currentDate())  # Set default date to today

        # Add the date edit to the layout
        self.date_layout.addWidget(self.date_edit)

        # Set the layout for the main window
        self.setLayout(self.date_layout)


    def save_date(self):
        # Get the selected date
        self.date = self.date_edit.date()

        # Convert the date to a string
        date_str = self.date.toString("yyyy-MM-dd")

        # Display the selected date in the label
        self.date_label.setText(f"Selected Date: {date_str}")
         

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config() 
    app = QApplication(sys.argv)
    window = search_bar()
    window.show()
    sys.exit(app.exec_())
