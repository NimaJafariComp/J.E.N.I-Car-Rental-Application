import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from .invoiceWindow import invoice_window
from ..api import api
    # Index 0: Car ID 
    # Index 1: Mileage
    # Index 2: MPG
    # Index 3: Price
    # Index 4: Car Year
    # Index 5: Car Model
    # Index 6: Car Make
    # Index 7: Car Color
    # Index 8: Car Type
class rent_window(QWidget):
    def __init__(self, customer_window, car, num_days, start_date, end_date):
        super().__init__()
        self.api = api()
        # setup main layout 
        self.customer_window = customer_window
        self.main_layout = QVBoxLayout(self)
        self.car = []
        self.car = car
        self.num_days = num_days
        self.start_date = start_date
        self.end_date = end_date

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)
        
        self.setup_main()

    def setup_form(self):
        self.form = QWidget()
        self.form_layout = QFormLayout(self.form)
        self.start     = QLabel("Pick Up Date: " + self.start_date.toString('yyyy-MM-dd'))
        self.end       = QLabel("Return Date: " + self.end_date.toString('yyyy-MM-dd'))
        self.Mileage   = QLabel("Mileage: " + str(self.car[1]))
        self.MPG       = QLabel("MPG: " + str(self.car[2]))
        self.Price     = QLabel("Price: " + str(self.car[3] * self.num_days))
        self.Car_Year  = QLabel("Car Year: " + str(self.car[4]))
        self.Car_Model = QLabel("Car Model: " + str(self.car[5]))
        self.Car_Make  = QLabel("Car Make: " + str(self.car[6]))
        self.Car_Color = QLabel("Car Color: " + str(self.car[7]))
        self.Car_Type  = QLabel("Car Type: " + str(self.car[8]))
        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.check_insurance = QCheckBox("Include Insurance")
        self.button_frame()
        self.form_layout.addRow(self.start)
        self.form_layout.addRow(self.end)
        self.form_layout.addRow(self.Mileage)
        self.form_layout.addRow(self.MPG)
        self.form_layout.addRow(self.Price)
        self.form_layout.addRow(self.Car_Year )
        self.form_layout.addRow(self.Car_Model)
        self.form_layout.addRow(self.Car_Make )
        self.form_layout.addRow(self.Car_Color)
        self.form_layout.addRow(self.Car_Type )
        self.form_layout.addRow(self.email)
        self.form_layout.addRow(self.check_insurance)
        self.form_layout.addRow(self.button_Qframe)
        self.make_button.clicked.connect(self.make_clicked)
        self.back_button.clicked.connect(self.back_clicked)
    

    def button_frame(self):
        self.button_Qframe = QFrame();
        self.button_layout = QHBoxLayout(self.button_Qframe)
        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.back_button.setFont(self.font)
        self.back_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.back_button.setFixedSize(200,50)

        self.make_button = QPushButton("Make Reservation")
        self.make_button.setFixedSize(200,50)
        self.make_button.setFont(self.font)
        self.make_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.button_layout.addWidget(self.back_button, alignment=Qt.AlignCenter)
        self.button_layout.addWidget(self.make_button, alignment=Qt.AlignCenter)


    def setup_main(self):
        self.setup_form()
        self.main_layout.addWidget(self.form, alignment=Qt.AlignCenter)

    def make_clicked(self):
        self.rent_window = invoice_window(self.customer_window, self.car, self.num_days, self.start_date, self.end_date, self.check_insurance.isChecked())
        self.customer_window.bottom_layout.removeWidget(self.customer_window.bottom_layout.widget(4)) 
        self.customer_window.bottom_layout.insertWidget(4, self.rent_window)
        self.customer_window.bottom_layout.setCurrentIndex(4)
        self.api.car_rental_obj.make_reservation(self.start_date.toString('yyyy-MM-dd'), self.end_date.toString('yyyy-MM-dd'), self.check_insurance.isChecked(), self.email.text(), self.car[0])

    def back_clicked(self):
        self.customer_window.bottom_layout.setCurrentIndex(1)

 
if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    list = []
    window = rent_window()
    window.show()
    sys.exit(app.exec_())
