from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

class admin_window(QWidget):
    def __init__(self):
        super().__init__()
        self.admin_layout = QVBoxLayout(self)
        
        self.top_frame = QFrame(self)
        self.top_frame.setMaximumSize(QSize(16777215,50))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)

        self.top_frame_layout = QHBoxLayout(self.top_frame)
        spacerItem = QSpacerItem(501, 20, QSizePolicy.Expanding, QSizePolicy.Minimum) 
        self.top_frame_layout.addItem(spacerItem)
        self.customer_button = QPushButton("Customer", self.top_frame)
        self.top_frame_layout.addWidget(self.customer_button)

        self.bottom_frame = QFrame(self)
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

        self.admin_layout.addWidget(self.top_frame)
        self.admin_layout.addWidget(self.bottom_frame)
