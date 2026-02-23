#PROBABILITY OF OCCUPANCY OF STATES

import numpy as np
import matplotlib.pyplot as plt

#Define the number of energy levels
N = 5000

#Define the energy spacing
E = 1.0

#Define the energy levels
energy_levels = E*np.arange(N)

#Define the temperatures
T_low = 200
T_high = 800

#Calculate the probabilities of occupancy at low temperature
prob_low_T = np.exp(-energy_levels/T_low)/np.sum(np.exp(-energy_levels/T_low))

#Calculate the probabilities of occupancy at high temperature
prob_high_T = np.exp(-energy_levels/T_high)/np.sum(np.exp(-energy_levels/T_high))

#Plot the results
plt.figure(figsize=(10,6))

plt.subplot(1,2,1)
plt.plot(energy_levels, prob_low_T)
plt.title('Occupancy at low temperature')
plt.xlabel('Energy level')
plt.ylabel('Probability of occupancy')


plt.subplot(1,2,2)
plt.plot(energy_levels, prob_high_T)
plt.title('Occupancy at high temperature')
plt.xlabel('Energy level')
plt.ylabel('Probability of occupancy')

plt.tight_layout()
plt.show()