from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class delete_car(QWidget):
    def __init__(self):
        super().__init__()

        # Main Layout for the Widget
        # self.layout() = QVBoxLayout()

        #Form Layout for input fields
        self.form_layout = QFormLayout()

        #Input field for VIN to delete a car (simple ex)
        self.vin_input = QLineEdit()
        self.vin_input.setPlaceholderText("Enter VIN of the car to delete")

        #Add the input field to the form layout
        self.form_layout.addRow("VIN", self.vin_input)

        #Create a button to submit the deletion request
        self.delete_button = QPushButton("Delete car")
        self.delete_button.clicked.connect(self.delete_car_from_inventory)

        #Add the form and button to the main layout
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.delete_button)

        #Set the layout for the widget
        self.setLayout(self.layout)

    def delete_car_from_inventory(self):
        #Retrieve the VIN from the input field
        vin = self.vin_input.text()

        #Error handling if VIN is empty
        if not vin:
            print("VIN field is empty. Please enter a valid VIN.")
            return
        #Simulate deletion logic(since no actual database or car list is provided)
        print(f"Simulated deletion of car with VIN {vin}.")

        #Optionally, clear the infield after deletion
        self.clear_input_field()

    def clear_input_field(self):
        """CLear the VIN field after the car is deleted."""
        self.vin_input_clear()
        
if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = delete_car()
    window.show()
    sys.exit(app.exec_())
