import math

def analytical_integral(a, b):
   return -math.cos(b) + math.cos(a)

# Parameters
a = 0
b = 1

# Calculate the analytical integral
integral = analytical_integral(a, b)
print(f"Analytical integral of sin(x) from {a} to {b} = {integral}")