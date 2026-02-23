
import math

def analytical_integral(a, b):
     return math.atan(b) -math.atan(a)
# Parameters
a = 0
b = 1

# Calculate the analytical integral
integral = analytical_integral(a, b)
print(f"Analytical integral of 1/(1+x^2) from {a} to {b} = {integral}")