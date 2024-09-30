import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from customerWindow import customer_window
from adminWindow import admin_window

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1155, 912)
        self.setStyleSheet("background-color:rgb(255, 255, 255)")

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.stacked_widget = QStackedLayout(self.central_widget)
        self.stacked_widget.setObjectName("stacked_widget")
        
        self.setCentralWidget(self.central_widget)

        self.c_window = customer_window()
        self.a_window = admin_window()
        self.stacked_widget.addWidget(self.c_window)
        self.stacked_widget.addWidget(self.a_window)
        self.stacked_widget.setCurrentIndex(0) 

        self.c_window.admin_button.clicked.connect(self.on_click_admin)
        self.a_window.customer_button.clicked.connect(self.on_click_customer)


    def on_click_admin(self):
        self.stacked_widget.setCurrentIndex(1)

    def on_click_customer(self):
        self.stacked_widget.setCurrentIndex(0)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())
