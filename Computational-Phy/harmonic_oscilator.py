import numpy as np
import scipy.integrate as intgr
import matplotlib.pyplot as plt

# Define the system of differential equations (no damping)
def equations(X, t, K1, m1):
    x1, v1 = X            # Unpack the state variables: position (x1) and velocity (v1)
    dx1 = v1              # Derivative of position is velocity
    dv1 = -K1/m1 * x1     # Derivative of velocity (acceleration), no damping term
    dXdt = [dx1, dv1]     # Return the derivatives as a list
    return dXdt

# Define constants
K1 = 1                    # Spring constant
m1 = 1                    # Mass

# Initial conditions
x1i = 0.2                # Initial position
v1i = 0                  # Initial velocity
init = [x1i, v1i]        # Initial state vector

# Time settings
T = 50.0                 # Total simulation time
time = np.arange(0, T, 0.01)   # Time array from 0 to T with 0.01s steps

# Solve the ODE
sol = intgr.odeint(equations, init, time, args=(K1, m1))                # Integrate the system
X = sol[:, 0]                                                           # Extract position values (first column)

# Plotting the result
plt.figure()
plt.plot(time, X, label='Y1 (no damping)')                               # Plot position vs. time
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.legend(loc='upper right')
plt.title('Simple Harmonic Oscillator (No Damping)')
plt.show()