from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QComboBox
from PySide6.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class UIHandler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LUTool')
        self.setGeometry(100, 100, 400, 600)

        self.layout = QVBoxLayout()
        self.setup_ui()
        self.setLayout(self.layout)

    def setup_ui(self):
        self.function_label = QLabel('Enter function using x, ex: "x * sin(x ** 2)"):')
        self.function_input = QLineEdit(self)

        self.filename_label = QLabel('Enter the filename:')
        self.filename_input = QLineEdit('output')

        self.output_label = QLabel('Select output folder:')
        self.output_button = QPushButton('Browse')
        self.output_button.clicked.connect(self.browse_output_folder)

        self.selected_path_label = QLabel('No folder selected.')

        self.preview_label = QLabel('Preview as:')
        self.preview_dropdown = QComboBox(self)
        self.preview_dropdown.addItems(["Image", "Graph"])

        self.preview_button = QPushButton('Generate Preview')
        self.generate_button = QPushButton('Generate LUT')

        self.output_width_label = QLabel('Output Width:')
        self.output_width_input = QLineEdit('32')  
        self.output_height_label = QLabel('Output Height:')
        self.output_height_input = QLineEdit('4')  

        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.filename_label)
        self.layout.addWidget(self.filename_input)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_button)
        self.layout.addWidget(self.selected_path_label)
        self.layout.addWidget(self.preview_label)
        self.layout.addWidget(self.preview_dropdown)
        self.layout.addWidget(self.preview_button)
        self.layout.addWidget(self.generate_button)

        self.layout.addWidget(self.output_width_label)
        self.layout.addWidget(self.output_width_input)
        self.layout.addWidget(self.output_height_label)
        self.layout.addWidget(self.output_height_input)

        self.preview_image_label = QLabel()
        self.layout.addWidget(self.preview_image_label)

        self.figure, self.ax = plt.subplots(figsize=(4, 2))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.hide()
        self.layout.addWidget(self.canvas)

    def browse_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
        if folder: 
            self.selected_path_label.setText(folder)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.preview_image_label.setPixmap(pixmap)
        self.canvas.hide()  
        self.preview_image_label.show()  

    def display_graph(self, func, width):
        x_vals = np.linspace(0, 2 * np.pi, width)
        y_vals = func(x_vals)

        self.ax.clear()

        self.ax.plot(x_vals, y_vals)
        self.canvas.draw()

        self.preview_image_label.hide()
        self.canvas.show()
