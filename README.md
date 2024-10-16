# LookupTableGenerator
 
This simple tool lets you create **Look-Up Tables from mathematical functions**. You can input any math function and once you're ready, just click the "Generate LUT" button, and the tool will create a grayscale image based on the function you provided. You can either use the **executable**(it's a stand-alone file) or directly run the **python script** (in that case you'll have to download the following libraries: *numpy matplotlib sympy PySide6*).

![image](https://github.com/user-attachments/assets/a9760154-efaa-4af4-b817-7ac89d5d35d5)

![output](https://github.com/user-attachments/assets/a222b4d2-440c-4da1-b363-b725179f73a5)

![output](https://github.com/user-attachments/assets/6861e282-874f-488e-ac4f-4d4998043eab)

![output](https://github.com/user-attachments/assets/4d193cdf-b8e3-4030-91b8-e33df0b9965b)


# Little message
The tool is far from being perfect, in case you have any suggestions feel free to ask a pull request or simply contact me. The code is accesible to everyone.

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
- Cosecant: csc(x) (1/sin(x))
- Secant: sec(x) (1/cos(x))
- Cotangent: cot(x) (1/tan(x))
- Arcsine: asin(x)
- Arccosine: acos(x)
- Arctangent: atan(x)
- Arccosecant: acsc(x)
- Arcsecant: asec(x)
- Arccotangent: acot(x)
Exponential and Logarithmic Functions
- Exponential: exp(x) (e^x)
- Natural Logarithm: log(x) (ln(x))
- Common Logarithm: log10(x) (base 10)
- Logarithm with Base: log(x, base)
### Hyperbolic Functions
- Hyperbolic Sine: sinh(x)
- Hyperbolic Cosine: cosh(x)
- Hyperbolic Tangent: tanh(x)
- Hyperbolic Cosecant: csch(x) (1/sinh(x))
- Hyperbolic Secant: sech(x) (1/cosh(x))
- Hyperbolic Cotangent: coth(x) (1/tanh(x))
- Inverse Hyperbolic Sine: asinh(x)
- Inverse Hyperbolic Cosine: acosh(x)
- Inverse Hyperbolic Tangent: atanh(x)
### Additional Functions
- Absolute Value: abs(x)
- Floor: floor(x)
- Ceiling: ceil(x)
- Round: round(x, n)
- Polynomial Functions: x**2 + 2*x + 1.
- Square Root: sqrt(x)
- Step : heaviside(x)
