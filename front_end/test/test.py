import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a frame
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)  # Set frame style (optional)

        # Create a layout and add the frame to it
        layout = QVBoxLayout()
        layout.addWidget(frame)  # Add frame to the layout

        # Set the layout on the central widget
        central_widget.setLayout(layout)

        # Make the window size adjustable
        self.setWindowTitle("QFrame Full Window")
        self.setGeometry(100, 100, 600, 400)  # Set the initial window size

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

