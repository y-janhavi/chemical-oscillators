import numpy as np
import scipy.integrate as intgr
import matplotlib.pyplot as plt

# Lotka Model Reactions
 
#   Y1 ------>  2Y1                            #  Prey Reproduction

#   Y1 + Y2 ------> Y1 + Y2                    #  Predation

#   Y2 ------> ∅                               #  Predator Mortality



# Define the system of differential equations
def equations(x, t, k1, k2, k3):  
    y1, y2 = x  # Unpack the variables
    dy1dt = k1 * y1 - k2 * y1 * y2              # Rate equation for y1
    dy2dt = k2 * y1 * y2 - k3 * y2              # Rate equation for y2
    return [dy1dt, dy2dt]

# Define parameters
k1, k2, k3 = 5, 4, 1                            # Reaction rate constants

# Initial conditions for y1 and y2
init = [0.13706323027549128, 0.4682405161100677]

# Define time range for the simulation
T = 15.0                                        # Total simulation time
time = np.arange(0, T, 0.01)                    # Time steps from 0 to T with step size 0.01

# Solve the differential equations using odeint
sol = intgr.odeint(equations, init, time, args=(k1, k2, k3))

# Extract solutions for y1 and y2 over time
y1t = sol[:, 0]  
y2t = sol[:, 1]  

# Plot the results
plt.figure()
plt.plot(time, y1t, label='Y1')                 # Plot Y1 over time
plt.plot(time, y2t, label='Y2')                 # Plot Y2 over time
plt.xlabel('Time')  
plt.ylabel('Population')  
plt.title("Lotka Model")
plt.legend(loc='upper right')                    # Add legend to the plot
plt.show()                                       # Display the plot

# Phase plot: Y2 vs. Y1
plt.plot(y2t, y1t)
plt.xlabel("Y2 (Predator)")
plt.ylabel("Y1 (Prey)")
plt.title("Phase Plot: Y2 vs. Y1")
plt.show()