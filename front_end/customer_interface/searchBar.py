from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ..config.font import font

class search_bar(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QHBoxLayout(self)
        self.setFixedSize(800, 100)

        self.date = date_picker()

        self.main_layout.addWidget(self.date)
    
class date_picker(QWidget):
    def __init__(self):
        super().__init__()
        self.dateedit = QDateEdit(calendarPopup=True)
        #self.menuBar().setCornerWidget(self.dateedit, Qt.TopLeftCorner)
        self.dateedit.setDateTime(QDateTime.currentDateTime())

if __name__ == "__main__":
    import sys
    from ..config.screenConfig import screen_config
    screen_config = screen_config() 
    app = QApplication(sys.argv)
    window = search_bar()
    window.show()
    sys.exit(app.exec_())
