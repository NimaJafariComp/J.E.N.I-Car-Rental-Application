from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from .addCar import add_car
from .reservations import reservations
from .transitionWindow import transition

class selection_window(QWidget):
    def __init__(self, admin_window):
        super().__init__()
        # setup main window layout
        self.admin_window = admin_window
        self.main_layout = QGridLayout(self)
        self.setFixedSize(1920,1080) 

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 25)

        # setup main widget
        self.setup_buttons()
        
    def setup_buttons(self):
        # add button
        self.add_button = QPushButton("Add Car")
        self.add_button.setFixedSize(200,150)
        self.add_button.setFont(self.font)
        self.add_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.main_layout.addWidget(self.add_button, 0, 0)
        self.add_button.clicked.connect(self.clicked_add)

        # delete button
        self.delete_button = QPushButton("Delete Car")
        self.delete_button.setFixedSize(200,150)
        self.delete_button.setFont(self.font)
        self.delete_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.main_layout.addWidget(self.delete_button, 0, 1)

        # reservations button
        self.reservations_button = QPushButton("reservations")
        self.reservations_button.setFixedSize(200,150)
        self.reservations_button.setFont(self.font)
        self.reservations_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.main_layout.addWidget(self.reservations_button, 0, 2)
        self.reservations_button.clicked.connect(self.clicked_reservation)

    def clicked_add(self):
        self.add_car = add_car()
        self.addcar_window = transition(self.admin_window, self.add_car, 1)
        self.admin_window.bottom_layout.removeWidget(self.admin_window.bottom_layout.widget(1)) 
        self.admin_window.bottom_layout.insertWidget(1, self.addcar_window)
        self.admin_window.bottom_layout.setCurrentIndex(1)

    def clicked_reservation(self):
        self.reservation = reservations()
        self.reservation_window = transition(self.admin_window, self.reservation, 0)
        self.admin_window.bottom_layout.removeWidget(self.admin_window.bottom_layout.widget(2)) 
        self.admin_window.bottom_layout.insertWidget(2, self.reservation_window)
        self.admin_window.bottom_layout.setCurrentIndex(2)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = selection_window()
    window.show()
    sys.exit(app.exec_())
