from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from font import font

class delete_car(QWidget):
    def __init__(self):
        super().__init__()
    

if __name__ == "__main__":
    import sys
    from screenConfig import screen_config
    screen_config = screen_config()
    app = QApplication(sys.argv)
    window = delete_car()
    window.show()
    sys.exit(app.exec_())
