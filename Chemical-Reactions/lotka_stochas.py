import math
import random
import matplotlib.pyplot as plt

# Lotka Model Reactions
 
#   Y1 ------>  2Y1                       #  Prey Reproduction

#   Y1 + Y2 ------> Y1 + Y2              #  Predation

#   Y2 ------> ∅                         #  Predator Mortality




# Initial concentrations of species Y1 (prey) and Y2 (predator)
Y1 = 1000  # Prey population
Y2 = 1000  # Predator population

# Rate constants for the reactions
k1 = 10    # Natural growth rate of Y1
k2 = 0.01  # Rate at which Y1 and Y2 interact
k3 = 10    # Natural death rate of Y2

# Time parameters
t_initial = 0  # Start time
t_final = 10   # End time

# Lists to store time points and species populations
t_points = [t_initial]
Y1_values = [Y1]
Y2_values = [Y2]

# Simulate the system over time
while t_initial < t_final and (Y1 > 0 or Y2 > 0):
    # Calculate propensity functions
    a1 = k1 * Y1  # Rate of Y1 birth
    a2 = k2 * Y1 * Y2  # Rate of Y1 and Y2 interaction
    a3 = k3 * Y2  # Rate of Y2 death
    a0 = a1 + a2 + a3  # Total rate

    # Generate random numbers for stochastic simulation
    r1 = random.uniform(0, 1)
    if a0 > 0:
        tau = (1 / a0) * math.log(1 / r1)  # Time step
    else:
        tau = float('inf')  # No event if total rate is zero

    # Update time
    t_initial += tau

    # Generate another random number to determine the event
    r2 = random.uniform(0, 1)

    # Determine which event occurs based on r2
    if r2 * a0 < a1:
        Y1 += 1  # Y1 reproduces
    elif r2 * a0 < a1 + a2:
        Y2 += 1  # Y2 reproduces
        Y1 -= 1  # Y1 is consumed
    elif r2 * a0 < a1 + a2 + a3:
        Y2 -= 1  # Y2 dies

    # Record the new state
    t_points.append(t_initial)
    Y1_values.append(Y1)
    Y2_values.append(Y2)

# Plot the population of Y1 over time
plt.plot(t_points, Y1_values, label='Y1 (Prey)')
plt.plot(t_points, Y2_values, label='Y2 (Predator)')
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.legend()
plt.show()

# Phase plot: Y2 vs. Y1
plt.plot(Y2_values, Y1_values)
plt.xlabel("Y2 (Predator)")
plt.ylabel("Y1 (Prey)")
plt.title("Phase Plot: Y2 vs. Y1")
plt.show()
