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
        self.reservations = self.api.car_rental_obj.get_reservations()
        self.delete_button = QPushButton("Delete")
        self.check_box = []
        self.button_style = "background-color: #efbe25; color: white; border: none; border-radius : 5px;"

        # centeral widget
        self.table = QTableWidget()

        # Make columns stretch to fill the width
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.setup_table()

    def setup_table(self):
        self.table.setRowCount(len(self.reservations)+1)
        self.table.setColumnCount(8)

        # Set the column headers
        self.table.setHorizontalHeaderLabels(['Reservation Id', 'Start Date', 'End Date', 'Insurance', 'CustomerEmail', 'Car ID', 'Price', 'Check'])
        self.table.verticalHeader().setVisible(False)


        for row, (reservations, start, end, idk, insurance, customerEmail, carID, idk2, price, idk3) in enumerate(self.reservations):
            self.table.setItem(row, 0, QTableWidgetItem(str(reservations)))
            self.table.setItem(row, 1, QTableWidgetItem(str(start.strftime("%Y-%m-%d"))))
            self.table.setItem(row, 2, QTableWidgetItem(str(end.strftime("%Y-%m-%d"))))
            self.table.setItem(row, 3, QTableWidgetItem(str(idk)))
            self.table.setItem(row, 4, QTableWidgetItem(customerEmail))
            self.table.setItem(row, 5, QTableWidgetItem(str(carID)))
            self.table.setItem(row, 6, QTableWidgetItem(str(price)))
            self.check_box.append(QCheckBox())
            self.table.setCellWidget(row, 7, self.check_box[row])

        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.delete_button, alignment=Qt.AlignCenter)
        self.delete_button.setStyleSheet(self.button_style)
        self.delete_button.setFixedWidth(150)
        self.delete_button.setFixedHeight(30)
        self.delete_button.clicked.connect(self.click_delete)

    def click_delete(self):
        for i in range(len(self.check_box)):
            if self.check_box[i].isChecked():
                print(self.reservations[i][0])

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = reservations()
    window.show()
    sys.exit(app.exec_())
