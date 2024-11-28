from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..api import api

class reservations(QWidget):
    def __init__(self):
        super().__init__()
        # setup main window layout
        self.main_layout = QVBoxLayout(self)
        self.api = api()
        self.reservations = []
        self.reservations = self.api.car_rental_obj.get_reservations()

        # centeral widget
        self.table = QTableWidget()

        # Make columns stretch to fill the width
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.setup_table()

    def setup_table(self):
        self.table.setRowCount(len(self.reservations)+1)
        self.table.setColumnCount(7)

        # Set the column headers
        self.table.setHorizontalHeaderLabels(['Reservation Id', 'Start Date', 'End Date', 'Insurance', 'CustomerEmail', 'Car ID', 'Price'])
        self.table.verticalHeader().setVisible(False)

        for row, (reservations, start, end, idk, insurance, customerEmail, carID, idk2, price) in enumerate(self.reservations):
            self.table.setItem(row, 0, QTableWidgetItem(str(reservations)))
            self.table.setItem(row, 1, QTableWidgetItem(str(start.strftime("%Y-%m-%d"))))
            self.table.setItem(row, 2, QTableWidgetItem(str(end.strftime("%Y-%m-%d"))))
            self.table.setItem(row, 3, QTableWidgetItem(str(idk)))
            self.table.setItem(row, 4, QTableWidgetItem(customerEmail))
            self.table.setItem(row, 5, QTableWidgetItem(str(carID)))
            self.table.setItem(row, 6, QTableWidgetItem(str(price)))

        self.main_layout.addWidget(self.table)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = reservations()
    window.show()
    sys.exit(app.exec_())
