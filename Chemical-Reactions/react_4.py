# SIMULATION OF 4-REACTION MODEL USING STANDARD ODE SOLVER IN PYTHON

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the system of differential equations
def equations(t,y):
    k1, k2, k3, k4 = 1, 0.002, 0.5, 0.04 # Rate constant
    y1, y2, y3 = y # Unpack the current state
    dy1dt = -k1*y1 - 2*k2*y1**2 + k3*2*y2 # Defferntial reaction-rate equation for y1 molecule
    dy2dt = k2*y1**2 - k3*y2 - k4*y2 # Defferntial reaction-rate equation for y2 molecule
    dy3dt = k4*y2 # Defferntial reaction-rate equation for y3 molecule
    return(dy1dt,dy2dt,dy3dt) # Return the derivatives

# Define the initial states
y0 = [100000, 0, 0]

# Define time parameters
T = 100.0
time_span = (0,T)
time_eval = np.arange(0,T,0.001)

# Solve ordinary differential equation using runge kutta 4th order method
sol = solve_ivp(equations, time_span, y0, method= 'RK45', t_eval=time_eval)

# Extract the solutions
y1t = sol.y[0]
y2t = sol.y[1]
y3t = sol.y[2]
time = sol.t

# Plot the result
plt.figure(figsize=(8,8))
plt.plot(time, y1t, label ='Y1')
plt.plot(time, y2t, label ='Y2')
plt.plot(time, y3t, label ='Y3')
plt.xlabel('time')
plt.ylabel('population')
plt.legend(loc = 'upper right')
plt.show()
