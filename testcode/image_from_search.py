import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from io import BytesIO
import pyodbc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add the datatools directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools')))

from datagrabber import DataGrabber
from imagewidget import ImageWidget

# Get the image URL from the database
data_grabber = DataGrabber()
data = data_grabber.get_data("sp_GetSpeciesImage", ["nerodia"])
image_url = data.iloc[0, 0].strip()  # Ensure the URL is properly formatted

# Load the image widget
app = QApplication(sys.argv)
ui_file = "pictures_screen.ui"  # Path to your UI file
window = ImageWidget(image_url, ui_file)
window.setFixedSize(800, 600)
window.show()

sys.exit(app.exec_())