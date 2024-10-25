from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class add_car(QWidget):
    def __init__(self):
        super().__init__()

        #Main Layout for the Widget
        #self.layout() = QVBoxLayout()

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
        self.car_type_input = QLineEdit()

        #Add placeholders to guide user input
        self.vin_input.setPlaceholderText("VIN")
        self.mileage_input.setPlaceholderText("Mileage")
        self.mpg_input.setPlaceholderText("MPG")
        self.price_input.setPlaceholderText("Price")
        self.license_plate_input.setPlaceholderText("License Plate")
        self.car_type_input.setPlaceholderText("Car Year")
        self.model_input.setPlaceholderText("Model")
        self.make_input.setPlaceholderText("Make")
        self.color_input.setPlaceholderText("Color")
        self.car_type_input.setPlaceholderText("Car Type")

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

        #Add the form and button to the main layout
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.add_button)

        #Set the layout for the widget
        self.setLayout(self.layout)

    def add_car_to_inventory(self):
        #Retrieve input date from fields
        vin = self.vin_input.text()
        mileage = int(self.mileage_input.text())
        mpg = int(self.mpg_input.text())
        price = float(self.price_input.text())
        license_plate = self.license_plate_input.text()
        car_year = int(self.car_year_input.text())
        model = self.model_input.text()
        make = self.make_input.text()
        color = self.color_input.text()
        car_type = self.car_type_input.text()

        #Create a new Car object using the input data
        new_car = car(vin, mileage, mpg, price, license_plate, car_year, model, make, color, car_type)

        #Log car details
        print("New car added:")
        print(new_car)

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
