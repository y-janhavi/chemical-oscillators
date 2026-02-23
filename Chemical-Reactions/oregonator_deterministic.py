# DETERMINISTIC SIMULATION OF COUPLED CHEMICAL REACTION - OREGONATOR REACTION MODEL

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Reactions
# X1 + Y2 ------> Y1 with reaction rate k1
# Y1 + Y2 ------> Z1 with reaction rate k2
# X2 + Y1 ------> 2Y1 + Y3 with reaction rate k3
# 2Y1 ------> Z2 with reaction rate k4
# X3 + Y3 ------> Y2 with reaction rate k5

# Define the system of differential equations
def equations(t,y):
    k1, k2, k3, k4, k5 = 2, 0.1, 104, 0.016, 26 # Parameters
    y1, y2, y3 = y # Unpack the current state
    
    dy1dt = k1*y2 - k2*y1*y2 + k3*y1 - 2*(k4/2)*y1*y1 # Differential reaction-rate equation of Y1
    dy2dt = -k1*y2 - k2*y2*y1 + k5*y3 # Differential reaction-rate equation of Y2
    dy3dt = k3*y1 - k5*y3 # Differential reaction-rate equation of Y3
    
    return(dy1dt, dy2dt, dy3dt) # Return derivatives

# Initial conditions of y1, y2 and y3 molecules
y0 = [0.13706323027549128, 0.4682405161100677, 0.18749323027549128]

# Time parameters
T = 3.0
time_span = (0,T)
time_eval = np.arange(0,T,0.001)

# Solve differential equations using runge-kutta 4th order method
sol = solve_ivp(equations, time_span, y0, method= 'RK45', t_eval=time_eval)

# Extract the solutions
y1t = sol.y[0]
y2t = sol.y[1]
y3t = sol.y[2]
time = sol.t

# Plot the results
plt.figure()
plt.plot(time, y1t, label ='Y1')
plt.plot(time, y2t, label ='Y2')
plt.plot(time, y3t, label ='Y3')
plt.xlabel('time')
plt.ylabel('population')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.legend(loc = 'upper right')
plt.title('Oregonator model - Population vs time')
plt.show()

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(y1t, y2t, y3t,'hotpink')
ax.set_xlabel('number of Y1 molecules', fontsize = 6)
ax.set_ylabel('number of Y2 molecules', fontsize = 6)
ax.set_zlabel('number of Y3 molecules', fontsize = 6)
ax.set_title('Oregonator model - phase plot')
plt.show()