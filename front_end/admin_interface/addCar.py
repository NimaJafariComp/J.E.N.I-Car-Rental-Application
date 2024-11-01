from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from ..api import api

class add_car(QWidget):
    def __init__(self):
        super().__init__()
        # setup api to backend
        self.api = api()

        #Main Layout for the Widget
        self.setFixedSize(500,400)
        self.main_layout = QVBoxLayout()

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 20)

        #From layout to handle car details
        self.form_layout = QFormLayout()

        #Input fields for the car attributes
        self.vin_input = QLineEdit()
        self.mileage_input = QLineEdit()
        self.mpg_input = QLineEdit()
        self.price_input = QLineEdit()
        self.license_plate_input = QLineEdit()
        self.car_year_input = QLineEdit()
        self.model_input = QLineEdit()
        self.make_input = QLineEdit()
        self.color_input = QLineEdit()
        self.car_type_input = QComboBox()

        #Add placeholders to guide user input
        self.vin_input.setPlaceholderText("VIN")
        self.mileage_input.setPlaceholderText("Mileage")
        self.mpg_input.setPlaceholderText("MPG")
        self.price_input.setPlaceholderText("Price")
        self.license_plate_input.setPlaceholderText("License Plate")
        self.car_year_input.setPlaceholderText("Car Year")
        self.model_input.setPlaceholderText("Model")
        self.make_input.setPlaceholderText("Make")
        self.color_input.setPlaceholderText("Color")
        self.car_type_input.addItems(['Sedan', 'Truck', 'Coupe', 'SUV'])

        #Add rows of labels and input fields to the form layout
        self.form_layout.addRow("VIN:", self.vin_input)
        self.form_layout.addRow("Mileage:", self.mileage_input)
        self.form_layout.addRow("MPG:", self.mpg_input)
        self.form_layout.addRow("Price:", self.price_input)
        self.form_layout.addRow("License Plate:", self.license_plate_input)
        self.form_layout.addRow("Car Year:", self.car_year_input)
        self.form_layout.addRow("Model:", self.model_input)
        self.form_layout.addRow("Make:", self.make_input)
        self.form_layout.addRow("Color:", self.color_input)
        self.form_layout.addRow("Car Type:", self.car_type_input)

        #Create a button to submit the new car
        self.add_button = QPushButton("Add Car")
        self.add_button.clicked.connect(self.add_car_to_inventory)
        self.add_button.setFixedSize(150,50)
        self.add_button.setFont(self.font)
        self.add_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")

        #Add the form and button to the main layout
        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addWidget(self.add_button, alignment=Qt.AlignCenter)

        #Set the layout for the widget
        self.setLayout(self.main_layout)

    def add_car_to_inventory(self):
        #Retrieve input date from fields
        vin = self.vin_input.text()
        mileage = int(self.mileage_input.text())
        mpg = int(self.mpg_input.text())
        price = float(self.price_input.text())
        license_plate = self.license_plate_input.text()
        car_year = self.car_year_input.text()
        model = self.model_input.text()
        make = self.make_input.text()
        color = self.color_input.text()
        car_type = self.car_type_input.currentText()

        #Create a new Car object using the input data
        self.api.car_rental_obj.add_car(vin, mileage, mpg, price, license_plate, car_year, model, make, color, car_type)

        #Optionally, reset input fields after adding the car
        self.clear_input_fields()

    def clear_input_fields(self):
        """Clears all input feilds after a car is added"""
        self.vin_input.clear()
        self.mileage_input.clear()
        self.mpg_input.clear()
        self.price_input.clear()
        self.license_plate_input.clear()
        self.car_year_input.clear()
        self.model_input.clear()
        self.make_input.clear()
        self.color_input.clear()
        self.car_type_input.clear()

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = add_car()
    window.show()
    sys.exit(app.exec_())
