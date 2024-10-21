import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class car_tile(QWidget): 
    def __init__(self):
        super().__init__()
        # variables that need imput
        self.price = 300
        self.name = "Toyota Corolla"
        self.mpg = 29
        self.year = 2020
        self.type = "sedan"
        self.img_path = os.path.join(os.path.dirname(__file__), "car_img/corolla.jpg")

        self.setFixedSize(600,200)
        self.car_tile_layout = QHBoxLayout(self)
       
        self.img = QLabel(self)
        self.pixmap = QPixmap(self.img_path)
        self.middle = QFrame(self)
        self.middle_layout = QVBoxLayout(self.middle)
        self.right = QFrame(self)
        self.right_layout = QVBoxLayout(self.right)

        self.middle_setup()
        self.right_setup()
        self.img_setup()
        self.tile_setup()
       

    def middle_setup(self):
        self.middle.setFixedSize(250, 200)
        self.middle.setStyleSheet("border : 1px solid lightgrey;")
        self.name_label = QLabel(self.name, self)
        self.name_label.setStyleSheet("border: none; font-size: 20pt; font-weight: bold;")
        self.year_label = QLabel("year: "+str(self.year), self)
        self.year_label.setStyleSheet("border: none;")
        self.mpg_label = QLabel("MPG: "+str(self.mpg), self)
        self.mpg_label.setStyleSheet("border: none;")
        self.type_label = QLabel("Type: "+self.type, self)
        self.type_label.setStyleSheet("border: none;")
        self.middle_layout.addWidget(self.name_label)
        self.middle_layout.addWidget(self.year_label)
        self.middle_layout.addWidget(self.mpg_label)
        self.middle_layout.addWidget(self.type_label)

    def right_setup(self):
        self.right.setFixedSize(150, 200)
        self.right.setStyleSheet("border : 1px solid lightgrey; border-bottom-right-radius: 15px; border-top-right-radius: 15px")


#    def img_setup(self):
#
#        self.img.setPixmap(self.pixmap)
#        self.img.resize(self.pixmap.width(), self.pixmap.height())
#        self.scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)   # width, height
#        self.img.setPixmap(self.scaled_pixmap)
#        self.img.setStyleSheet("border : 1px solid lightgrey; border-bottom-left-radius: 15px; border-top-left-radius: 15px;")   
#        self.img.setFixedSize(200, 200)
#        self.img.setAlignment(Qt.AlignCenter)

    def tile_setup(self):
        self.car_tile_layout.setContentsMargins(0, 0, 0, 0)
        self.car_tile_layout.setSpacing(0)
        self.car_tile_layout.addWidget(self.img)
        self.car_tile_layout.addWidget(self.middle)
        self.car_tile_layout.addWidget(self.right)

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
    from screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = car_tile()
    window.show()
    sys.exit(app.exec_())
