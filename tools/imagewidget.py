import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from io import BytesIO

class ImageWidget(QMainWindow):
    def __init__(self, image_url, ui_file, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.image_url = image_url
        loadUi(ui_file, self)
        self.load_image()

    def load_image(self):
        try:
            response = requests.get(self.image_url)
            response.raise_for_status()
            image = QPixmap()
            image.loadFromData(BytesIO(response.content).read())
            self.imageLabel.setPixmap(image)  # Assuming the QLabel in the UI file is named 'imageLabel'
        except requests.exceptions.RequestException as e:
            self.imageLabel.setText(f"Failed to load image: {e}")

# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_url = "https://example.com/path/to/image.jpg"
    ui_file = "pictures_screen.ui"  # Path to your UI file
    window = ImageWidget(image_url, ui_file)
    window.setFixedSize(800, 600)
    window.show()
    sys.exit(app.exec_())