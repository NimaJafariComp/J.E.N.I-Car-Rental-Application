from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ..api import api
from ..config.font import font
from ..currentUser import CurrentUser


class reservations_history(QWidget):
    def __init__(self):
        super().__init__()

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        # setup main window layout
        self.main_layout = QVBoxLayout(self)
        self.api = api()

        self.button_style = "background-color: #efbe25; color: white; border: none; border-radius : 5px; outline: none;"

        # Make columns stretch to fill the width

    def setup_table(self, user_ID, name):
        Id = user_ID
        user_name = name
        self.clear_layout(self.main_layout)
        self.user_name = QLabel(user_name + "'s Reservation History:")
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.user_name.setFont(self.font)
        self.reservations = self.api.car_rental_obj.resevation_history(Id)
        self.main_layout.addWidget(self.user_name, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.table)
        self.table.setRowCount(0)
        self.table.setRowCount(len(self.reservations))
        self.table.setColumnCount(10)

        # Set the column headers
        self.table.setHorizontalHeaderLabels(
            [
                "Reservation Id",
                "Start Date",
                "End Date",
                "Insurance",
                "Customer ID",
                "CustomerEmail",
                "Car ID",
                "Price",
                "Canceled",
                "Checked Out",
            ]
        )
        self.table.verticalHeader().setVisible(False)

        for row, (
            id,
            start,
            end,
            insurance,
            customerID,
            customerEmail,
            carID,
            canceled,
            price,
            confirmed,
        ) in enumerate(self.reservations):
            self.table.setItem(row, 0, QTableWidgetItem(str(id)))
            self.table.setItem(
                row, 1, QTableWidgetItem(str(start.strftime("%Y-%m-%d")))
            )
            self.table.setItem(row, 2, QTableWidgetItem(str(end.strftime("%Y-%m-%d"))))
            self.table.setItem(row, 3, QTableWidgetItem(str(bool(insurance))))
            self.table.setItem(row, 4, QTableWidgetItem(str(customerID)))
            self.table.setItem(row, 5, QTableWidgetItem(customerEmail))
            self.table.setItem(row, 6, QTableWidgetItem(str(carID)))
            self.table.setItem(row, 7, QTableWidgetItem(str(price)))
            self.table.setItem(row, 8, QTableWidgetItem(str(bool(canceled))))
            self.table.setItem(row, 9, QTableWidgetItem(str(bool(confirmed))))

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
    window = reservations()
    window.show()
    sys.exit(app.exec_())
