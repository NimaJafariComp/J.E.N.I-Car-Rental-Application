import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel

class carTile_scroll(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setup scroll frame and layout
        self.scroll_frame = QWidget()
        self.scroll_frameLayout = QVBoxLayout(self.scroll_frame)

        # Setup main layout
        self.scroll_layout = QVBoxLayout(self)

        # Setup scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_frame)

        # Add scroll area to main layout
        self.scroll_layout.addWidget(self.scroll_area)

        # Set scroll area style
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 8px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background-color: #bfbfbf;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #999999;
            }
            QScrollBar::handle:vertical:pressed {
                background-color: #787878;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 8px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:horizontal {
                background-color: #bfbfbf;
                min-width: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:horizontal:hover {
                background-color: #999999;
            }
            QScrollBar::handle:horizontal:pressed {
                background-color: #787878;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                border: none;
                background: none;
            }
        """)

        # Add test items
        #self.test()

    def test(self):
        self.list = []  # Initialize as an empty list
        for i in range(20):
            label = QLabel(f"This is a test {i+1}")
            self.list.append(label)
            self.scroll_frameLayout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = carTile_scroll()
    window.show()
    sys.exit(app.exec_())

