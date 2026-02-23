import numpy as np
import scipy.integrate as intgr
import matplotlib.pyplot as plt

# Define the system of differential equations (with damping)
def equations(X, t, K1, m1, b1):
    x1, v1 = X            # Unpack the state variables: position (x1) and velocity (v1)
    dx1 = v1              # Derivative of position is velocity
    dv1 = (-K1/m1 * x1) - (b1/m1 * v1)  # Derivative of velocity (acceleration), with damping term (-b1*v1)
    dXdt = [dx1, dv1]     # Return the derivatives as a list
    return dXdt

# Define constants
K1 = 1    # Spring constant (N/m)
m1 = 1    # Mass (kg)
b1 = 0.1  # Damping coefficient (kg/s)

# Initial conditions
x1i = 0.2    # Initial position (m)
v1i = 0      # Initial velocity (m/s)
init = [x1i, v1i]    # Initial state vector

# Time settings
T = 50.0    # Total simulation time (seconds)
time = np.arange(0, T, 0.01)   # Time array from 0 to T with 0.01s steps

# Solve the ODE
sol = intgr.odeint(equations, init, time, args=(K1, m1, b1))  # Integrate the system
X = sol[:, 0]    # Extract position values (first column)

# Plotting the result
plt.figure()
plt.plot(time, X, label='Y1 (with damping)')  # Plot position vs. time
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend(loc='upper right')
plt.title('Damped Harmonic Oscillator')
plt.show()