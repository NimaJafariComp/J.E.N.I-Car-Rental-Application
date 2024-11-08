from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import shutil

class img_adder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Button to select JPG file
        self.select_button = QPushButton('Select JPG File')
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        # Label to show selected file
        self.file_label = QLabel('No file selected')
        layout.addWidget(self.file_label)

        # Image preview
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def select_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select JPG File", "", "JPEG Files (*.jpg);;All Files (*)", options=options)
        if file_path:
            self.file_path = file_path
            self.file_label.setText(f'Selected File: {os.path.basename(file_path)}')
            self.display_image(file_path)
        else:
            self.file_label.setText('No file selected')
            self.image_label.clear()

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))
        else:
            self.image_label.setText('Failed to load image')

    def save_file(self, vinNum):
        new_name = vinNum

        new_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "car_img/" + new_name + ".jpg")
        try:
            shutil.copy(self.file_path, new_file_path)
            QMessageBox.information(self, 'Success', f'File saved as: {new_file_path}')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save file: {str(e)}')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = img_adder()
    window.show()
    sys.exit(app.exec_())

