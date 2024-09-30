from PyQt5 import QtCore, QtGui, QtWidgets


class customer_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.customer_layout = QtWidgets.QVBoxLayout(self)

        self.top_frame = QtWidgets.QFrame(self)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.top_frame_layout = QtWidgets.QHBoxLayout(self.top_frame)
        spacerItem = QtWidgets.QSpacerItem(501, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.top_frame_layout.addItem(spacerItem)
        self.admin_button = QtWidgets.QPushButton("Admin",self.top_frame)
        self.top_frame_layout.addWidget(self.admin_button)

        self.customer_layout.addWidget(self.top_frame)

        self.bottom_frame = QtWidgets.QFrame(self)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.customer_layout.addWidget(self.bottom_frame)
