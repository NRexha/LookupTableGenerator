import numpy as np
import matplotlib.pyplot as plt
import os
from sympy import symbols, sympify
from sympy.utilities.lambdify import lambdify

x = symbols('x')

class LUTGenerator:
    def __init__(self, ui_handler):
        self.ui_handler = ui_handler
        self.ui_handler.preview_button.clicked.connect(self.generate_preview)
        self.ui_handler.generate_button.clicked.connect(self.generate_lut)

    def generate_preview(self):
        function_str = self.ui_handler.function_input.text()
        width = 512 
        height = 64  

        try:
            expr = sympify(function_str)
            func = lambdify(x, expr, 'numpy')

            lut_data = np.zeros((height, width, 3), dtype=np.uint8)
            for i in range(width):
                x_val = (i / (width - 1)) * (2 * np.pi)
                y_val = func(x_val)

                y_val = np.nan_to_num(y_val, nan=0.0, posinf=1.0, neginf=0.0)
                y_val = max(0, y_val) 

                color_value = int(y_val * 255) 

                for j in range(height):
                    lut_data[j, i] = [color_value, color_value, color_value]

            preview_type = self.ui_handler.preview_dropdown.currentText()

            if preview_type == "Image":
                temp_image_path = 'temp_lut_preview.png' 
                plt.imsave(temp_image_path, lut_data)
                self.ui_handler.display_image(temp_image_path)

            elif preview_type == "Graph":
                self.ui_handler.display_graph(func, width)

        except Exception as e:
            print(f"Couldn't generate preview: {e}")

    def generate_lut(self):
        function_str = self.ui_handler.function_input.text()
        width = int(self.ui_handler.output_width_input.text()) 
        height = int(self.ui_handler.output_height_input.text()) 
        filename = self.ui_handler.filename_input.text()

        output_path = self.ui_handler.selected_path_label.text()
        if not output_path or output_path == 'No folder selected.':
            return

        if not filename.endswith('.png'):
            filename += '.png'

        try:
            expr = sympify(function_str)
            func = lambdify(x, expr, 'numpy')

            lut_data = np.zeros((height, width, 3), dtype=np.uint8)
            for i in range(width):
                x_val = (i / (width - 1)) * (2 * np.pi)
                y_val = func(x_val)
                y_val = np.nan_to_num(y_val, nan=0.0, posinf=1.0, neginf=0.0)
                y_val = max(0, y_val)

                color_value = int(y_val * 255)

                for j in range(height):
                    lut_data[j, i] = [color_value, color_value, color_value]

            output_file = os.path.join(output_path, filename)
            plt.imsave(output_file, lut_data)

        except Exception as e:
            print(f"Couldn't generate LUT: {e}")
