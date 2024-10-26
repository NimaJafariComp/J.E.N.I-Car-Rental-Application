import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font
from .rentWindow import rent_window

class car_tile(QWidget): 
    def __init__(self, car, window, num_days, start_date, end_date):
        super().__init__()
        # knows customer window
        self.customer_window = window
        self.num_days = num_days
        self.start_date = start_date
        self.end_date = end_date

        # variables that need imput
        self.car = []
        self.car = car
        self.price = car[3]
        self.name = car[6] + " " + car[5]
        self.mpg = car[2]
        self.year = car[4]
        self.type = car[8]
        self.img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "car_img/corolla.jpg")

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.setFixedSize(600,200)
        self.car_tile_layout = QHBoxLayout(self)
       
        self.img = QLabel()
        self.pixmap = QPixmap(self.img_path)
        self.middle = QFrame()
        self.middle_layout = QVBoxLayout(self.middle)
        self.right = QFrame()
        self.right_layout = QVBoxLayout(self.right)

        self.middle_setup()
        self.right_setup()
        self.img_setup()
        self.tile_setup()
       

    def middle_setup(self):
        self.middle.setFixedSize(250, 200)
        self.middle.setStyleSheet("border : 1px solid lightgrey;")
        self.name_label = QLabel(self.name)
        self.name_label.setStyleSheet("border: none; font-size: 10pt; font-weight: bold;")
        self.year_label = QLabel("year: "+str(self.year))
        self.year_label.setStyleSheet("border: none;")
        self.mpg_label = QLabel("MPG: "+str(self.mpg))
        self.mpg_label.setStyleSheet("border: none;")
        self.type_label = QLabel("Type: "+self.type)
        self.type_label.setStyleSheet("border: none;")
        self.middle_layout.addWidget(self.name_label)
        self.middle_layout.addWidget(self.year_label)
        self.middle_layout.addWidget(self.mpg_label)
        self.middle_layout.addWidget(self.type_label)

    def right_setup(self):
        self.right.setFixedSize(150, 200)
        self.right.setStyleSheet("border : 1px solid lightgrey; border-bottom-right-radius: 15px; border-top-right-radius: 15px")
        self.rent_button = QPushButton('Rent')
        self.rent_button.setFont(self.font)
        self.rent_button.setStyleSheet("color: white; background:#efbe25; border-radius: 5px;")
        self.price_label = QLabel("Price: "+str(self.price)+"/per day")
        self.price_label.setStyleSheet("border: none;")
        self.right_layout.addWidget(self.price_label)
        self.right_layout.addWidget(self.rent_button)
        self.rent_button.clicked.connect(self.rent_clicked)

    def tile_setup(self):
        self.car_tile_layout.setContentsMargins(0, 0, 0, 0)
        self.car_tile_layout.setSpacing(0)
        self.car_tile_layout.addWidget(self.img)
        self.car_tile_layout.addWidget(self.middle)
        self.car_tile_layout.addWidget(self.right)
        
    def rent_clicked(self):
        self.rent_window = rent_window(self.customer_window, self.car, self.num_days, self.start_date, self.end_date)
        self.customer_window.bottom_layout.removeWidget(self.customer_window.bottom_layout.widget(3)) 
        self.customer_window.bottom_layout.insertWidget(3, self.rent_window)
        self.customer_window.bottom_layout.setCurrentIndex(3)
    

    def img_setup(self):
        # Set the size of the QLabel to match the QFrame
        self.img.setFixedSize(200, 200)
    
        # Scale the image to fully fill the QLabel, keeping aspect ratio
        self.scaled_pixmap = self.pixmap.scaled(self.img.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    
        # Create a QPixmap with rounded corners only on the left side
        rounded_pixmap = self.apply_rounded_mask(self.scaled_pixmap, self.img.size(), 15)  # Adjust the radius here to match the QFrame
    
        # Set the QPixmap with rounded corners to the QLabel
        self.img.setPixmap(rounded_pixmap)
        self.img.setStyleSheet("border: 1px solid lightgrey; border-bottom-left-radius: 15px; border-top-left-radius: 15px;")   
        self.img.setAlignment(Qt.AlignCenter)
    
    def apply_rounded_mask(self, pixmap, size, radius):
        """Applies a mask with rounded corners only on the left side and ensures the image fills the QLabel."""
        # Create a new transparent QPixmap with the same size as QLabel
        rounded_pixmap = QPixmap(size)
        rounded_pixmap.fill(Qt.transparent)
    
        # Set up the painter for drawing the rounded image
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
    
        # Create a path for rounding only the top-left and bottom-left corners
        path = QPainterPath()
    
        # Top-left corner
        path.moveTo(radius, 0)
        path.arcTo(0, 0, 2 * radius, 2 * radius, 90, 90)
    
        # Left side
        path.lineTo(0, size.height() - radius)
    
        # Bottom-left corner
        path.arcTo(0, size.height() - 2 * radius, 2 * radius, 2 * radius, 180, 90)
    
        # Bottom-right and top-right are sharp
        path.lineTo(size.width(), size.height())
        path.lineTo(size.width(), 0)
        path.lineTo(radius, 0)
    
        # Set the clipping path to ensure only the left corners are rounded
        painter.setClipPath(path)
    
        # Center the image in the QLabel
        x_offset = (size.width() - pixmap.width()) // 2
        y_offset = (size.height() - pixmap.height()) // 2
    
        # Draw the pixmap scaled to the QLabel's size
        painter.drawPixmap(x_offset, y_offset, pixmap)
    
        painter.end()
        return rounded_pixmap



if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    list = []
    window = car_tile(list)
    window.show()
    sys.exit(app.exec_())
