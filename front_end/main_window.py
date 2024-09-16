import sys

import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw


class main_window(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("J.E.N.I Car Rental")
        self.setGeometry(0, 0, 1920, 1080)
        self.center_window()

        self.show()

    def init_ui(self):
        pass

    def center_window(self):
        # Get the frame geometry of the window
        screen = self.frameGeometry()
        # Get the center of the screen
        screen_center = qtw.QApplication.desktop().screenGeometry().center()
        # Move the window frame's center to the screen center
        screen.moveCenter(screen_center)
        # Move the top-left of the window to the top-left of the frame
        self.move(screen.topLeft())


app = qtw.QApplication(sys.argv)
mw = main_window()

# run app
app.exec_()
