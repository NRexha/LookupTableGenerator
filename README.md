# LookupTableGenerator
 
This simple tool lets you create **Look-Up Tables from mathematical functions**. You can input any math function and check how it looks by using one of the preview modes. When you're happy with it, just click the "Generate LUT" button and the tool will create a grayscale image based on the function you provided. You can either use the **executable** and all you'll have to do is run the .exe file (you will need the "LUTool.exe" and the folder "_internal") or directly run the **python script** (dowload all the scripts and run "LUTool.py"), in that case you'll have to download the following libraries: *numpy matplotlib sympy PySide6*.

![Sans titre-1](https://github.com/user-attachments/assets/94c8c17b-90f1-4305-ae4c-090d28092144)

# Little message
The tool is far from being perfect, in case you have any suggestions feel free to ask a pull request or simply contact me. The code is accesible to everyone. I'll try to implement the following features when I'll have some free time:
- <del>Add preview as image/graph before generating </del>
- Being able to pack multiple LUTs in different rgb(a) channels
- Create different layers math func in one LUT (one in the first pixel row, on in the second etc...)


## Mathematical functions that you can input
<ins>**Ensure that you follow Python's syntax when inputting functions.</ins>** For example, use x * sin(x) for the function xsin(x)
### Basic Functions
- Addition: x + y
- Subtraction: x - y
- Multiplication: x * y
- Division: x / y
- Exponentiation: x ** y
### Trigonometric Functions
- Sine: sin(x)
- Cosine: cos(x)
- Tangent: tan(x)
### Logarithmic Functions
- Natural Logarithm: log(x) (ln(x))
- Common Logarithm: log10(x) (base 10)
- Logarithm with Base: log(x, base)
### Additional Functions
- Floor: floor(x)
- Ceiling: ceil(x)
- Square Root: sqrt(x)
- Step : heaviside(x)
