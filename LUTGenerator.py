import sys
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify
from sympy.utilities.lambdify import lambdify
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                               QLineEdit, QPushButton, QFileDialog)

#personal tool for creating Lookup tables. I created this in order to speed-up LUT for games, especially for shaders.
x = symbols('x')

class LUTGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('LUT Generator')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        #func input
        self.function_label = QLabel('Enter function using x (ex: "x * sin(x ** 2)"):')
        self.function_input = QLineEdit(self)

        #tex size
        self.width_label = QLabel('Enter width (ex: "32"):')
        self.width_input = QLineEdit('32')
        self.height_label = QLabel('Enter height (ex: "4"):')
        self.height_input = QLineEdit('4')

        #tex name
        self.filename_label = QLabel('Enter the filename (ex: "lut.png"):')
        self.filename_input = QLineEdit('output.png')

        #output path
        self.output_label = QLabel('Select output folder:')
        self.output_button = QPushButton('Browse')
        self.output_button.clicked.connect(self.browse_output_folder)
        self.output_path = ''  # Initialize output path
        self.selected_path_label = QLabel('No folder selected.')

        #lut generation
        self.generate_button = QPushButton('Generate LUT')
        self.generate_button.clicked.connect(self.generate_lut)


        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        layout.addWidget(self.filename_label)
        layout.addWidget(self.filename_input)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_button)
        layout.addWidget(self.selected_path_label)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def browse_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
        if folder: 
            self.output_path = folder
            self.selected_path_label.setText(folder)

    def generate_lut(self):
        # Get user inputs
        function_str = self.function_input.text()
        width = int(self.width_input.text())
        height = int(self.height_input.text())
        filename = self.filename_input.text()

        if not self.output_path:
            print("You need to define a path for generating the LUT")
            return

        try:
            #input to func
            expr = sympify(function_str)
            func = lambdify(x, expr, 'numpy')

            #write LUT
            lut_data = np.zeros((height, width, 3), dtype=np.uint8)
            for i in range(width):
                x_val = (i / (width - 1)) * (2 * np.pi)  #normalize x to [0, 2π]
                y_val = func(x_val)
                
                #map between [0,255]
                if isinstance(y_val, (list, tuple, np.ndarray)):
                    y_val = y_val[0]
                y_val = np.clip(y_val, -1, 1)  #clip to [-1, 1]
                color_value = int((y_val + 1) / 2 * 255)  #scale to [0, 255]

                for j in range(height):
                    lut_data[j, i] = [color_value, color_value, color_value]

            #svae LUT tex
            output_file = f"{self.output_path}/{filename}"
            plt.imsave(output_file, lut_data)
            print(f"LUT saved as {output_file}")
        except Exception as e:
            print(f"Couldn't generate LUT: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = LUTGenerator()
    generator.show()
    sys.exit(app.exec())
