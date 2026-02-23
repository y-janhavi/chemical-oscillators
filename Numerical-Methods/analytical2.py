
import math

def analytical_integral(a, b):

     return (b**4/4) - (a**4/4)

# Parameters
a = 0
b = 1

# Calculate the analytical integral
integral = analytical_integral(a, b)
print(f"Analytical integral of x^3 from {a} to {b} = {integral}")