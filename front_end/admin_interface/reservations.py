from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class reservations(QWidget):
    def __init__(self):
        super().__init__()
        # setup main window layout
        self.main_layout = QVBoxLayout(self)
        self.reservations = []

        # centeral widget
        self.table = QTableWidget()

    def setup_table(self):
        self.table.setRowCount(len(self.reservations))
        self.table.setColumnCount(5)

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = reservations()
    window.show()
    sys.exit(app.exec_())
