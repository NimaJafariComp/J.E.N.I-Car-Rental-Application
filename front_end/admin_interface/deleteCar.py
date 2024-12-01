from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from ..api import api

class delete_car(QWidget):
    def __init__(self):
        super().__init__()
        #Setup API to backend
        self.api = api()
        #Main layout for the widget
        self.setFixedSize(800, 400)
        self.main_layout = QVBoxLayout(self)

        #Setup font
        self.set_font = font()
        #self.font() == QFont(self.set_font.font_family, 16)
        self.font = QFont(self.set_font.font_family, 16)

        #Table to display cars with checkboxes
        self.car_table = QTableWidget()
        self.car_table.setColumnCount(6) #Example: VIN, Model, Make, Year, Color, Select
        self.car_table.setHorizontalHeaderLabels(["VIN", "Model", "Make", "Year", "Color","Select"])
        self.car_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.car_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.car_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #Load car data into the table
        self.load_car_data()

        #Delete button
        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_selected_cars)
        self.delete_button.setFixedSize(200, 50)
        self.delete_button.setFont(self.font)
        self.delete_button.setStyleSheet("color: white; background:#ef4c25; border-radius: 5px;")

        #Add widgets to the main layout
        self.main_layout.addWidget(self.car_table)
        self.main_layout.addWidget(self.delete_button, alignment=Qt.AlignCenter)

    def load_car_data(self):
        """Loads car data into the table with checkboxes"""
        cars = self.api.car_rental_obj.get_all_cars() #Retrieve all cars from API
        self.car_table.setRowCount(len(cars))

        for row, car in enumerate(cars):
            self.car_table.setItem(row, 0, QTableWidgetItem(car["vin"]))
            self.car_table.setItem(row, 1, QTableWidgetItem(car["model"]))
            self.car_table.setItem(row, 2, QTableWidgetItem(car["make"]))
            self.car_table.setItem(row, 3, QTableWidgetItem(car["year"]))
            self.car_table.setItem(row, 4, QTableWidgetItem(car["color"]))

            #Add a checkbox for selection
            checkbox = QCheckBox()
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.addWidget(checkbox)
            checkbox_layout.setAlignment(Qt.AlignCenter)
            checkbox_layout.setContentsMargins(0, 0, 0, 0)
            self.car_table.setCellWidget(row, 5, checkbox_widget)

    def delete_selected_cars(self):
        """Delete selected cars based on checked checkboxes"""
        for row in range(self.car_table.rowCount()):
            checkbox_widget = self.car_table.cellWidget(row, 5)
            checkbox = checkbox_widget.findChild(QCheckBox)

            if checkbox.isChecked():
                vin = self.car_table.item(row, 0).text()  # Get VIN from the table

                try:
                    # Assuming the API has a delete method that takes VIN as a parameter.
                    self.api.car_rental_obj.delete_car(vin)  # Make sure this method is correct
                except AttributeError:
                    print(f"Error: The method 'delete_car' does not exist on the API object.")
                except Exception as e:
                    print(f"An error occurred while deleting the car with VIN {vin}: {e}")

                # Refresh the table after deletion
            self.load_car_data()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = delete_car()
    window.show()
    sys.exit(app.exec_())
