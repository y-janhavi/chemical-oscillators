# SIMULATION OF LAW OF RADIOACTIVE DECAY (A---->B)

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define differential equation for radioactive decay
def decay(y, t, k):
    # Unpack the variables
    A, B = y

    # Rate of change of A (decay) and B (formation)
    dAdt = -k*A
    dBdt = k*A
    return [dAdt, dBdt]

# Define parameters
k = 0.1 # Decay rate constant
A0 = 100 # Initial number of molecules of A
B0 = 0 # Initial number of molecules of B

# Initial conditions
y0 = [A0, B0] 

# Time points for simulations
t = np.linspace(0,50)

# Solve the ODE using odeint
sol = odeint(decay, y0, t, args=(k,))

# Plot the results
'''plt.plot(t, sol[:, 0], label ='A(t)') #Plot A over time
plt.plot(t, sol[:, 1], label ='B(t)') #Plot B over time'''
plt.xlabel('Time (t)')
plt.ylabel('Number of molecules')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.title('Radioactive Decay Simulations')
plt.legend(loc = 'upper right')
plt.show()