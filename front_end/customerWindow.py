from PyQt5 import QtCore, QtGui, QtWidgets


class customer_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.customer_layout = QtWidgets.QVBoxLayout(self)
        self.customer_layout.setContentsMargins(0, 0, 0, 0)
        self.customer_layout.setSpacing(0)

        self.top_frame = QtWidgets.QWidget(self)
        self.top_frame.setFixedHeight(100)
        self.top_frame.setStyleSheet(
            "background: grey;"
        )

        self.top_frame_layout = QtWidgets.QHBoxLayout(self.top_frame)
        spacerItem = QtWidgets.QSpacerItem(501, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top_frame_layout.addItem(spacerItem)
        self.admin_button = QtWidgets.QPushButton("Admin",self.top_frame)
        self.top_frame_layout.addWidget(self.admin_button)
        self.admin_button.setStyleSheet(
            "background: white;"
        )

        self.customer_layout.addWidget(self.top_frame)

        self.bottom_frame = QtWidgets.QFrame(self)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.customer_layout.addWidget(self.bottom_frame)
