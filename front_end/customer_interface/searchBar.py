from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class search_bar(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout(self)
        self.setFixedSize(800, 100)

        self.dateedit = QDateEdit(calendarPopup=True)
        self.menuBar().setCornerWidget(self.dateedit, Qt.TopLeftCorner)
        self.dateedit.setDateTime(QDateTime.currentDateTime())
    
class date_picker():

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config() 
    app = QApplication(sys.argv)
    window = search_bar()
    window.show()
    sys.exit(app.exec_())
