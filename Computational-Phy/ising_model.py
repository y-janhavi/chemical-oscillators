# SIMULATION OF 1D ISING MODEL

import numpy as np
import matplotlib.pyplot as plt

#Function to calculate Energy of the system
def cal_energy(spins,J,h):
    energy =0
    #Calculate energy by summing over all spins
    for i in range(len(spins)):
        energy+=J*spins[i]*spins[(i+1)%len(spins)]/N
        energy+=h*spins[i]/N
    #Return negative energy(convention in ising model)
    return -energy #Return negative energy(convention in ising model)

#Function to calculate Magnetisation
def cal_mag(spins):
    #Return absolute value of mean magnetisation
    return np.abs(np.mean(spins))

#Function to perform Metropolis Monte Carlo simulation
def metropolis_monte_carlo(spins,J,h,T,num_steps,equ_steps):
    #Initialize arrays to store energies and magnetisations
    energies=np.zeros(num_steps)
    magnetisations=np.zeros(num_steps)

    #Perform Monte carlo simulation
    for step in range(num_steps):
        i = np.random.randint(0,len(spins))

        #Calculate change in energy (deltaE)
        deltaE = 2*J*spins[i]*(spins[(i-1)%len(spins)]+spins[(i+1)%len(spins)])

        #Apply Metropolis criterion
        if deltaE <= 0 or np.random.rand() < np.exp(-deltaE/T):
            spins[i]*=-1

        #Calculate energy and magnetizations
        energies[step]=cal_energy(spins,J,h)
        magnetisations[step]=cal_mag(spins)

    #Return energies, magnetizations
    return energies,magnetisations

#Parameters
N = 100 #Number of lattice sites
J=1 #Coupling constant
h=0 #External magnetic field
T_range=np.linspace(0.1,10,100) #Temperature range
num_steps=10000 #Number of Monte Carlo steps
equ_steps = 1000 #Number of equilibrium steps

#Initialise Array to store data
E_avg = np.zeros(len(T_range))
M_avg = np.zeros(len(T_range))
X=np.zeros(len(T_range))
C=np.zeros(len(T_range))

#Loop over temprature
for i , T in enumerate(T_range):
    #Initialize spins
    spins=np.ones(N)
    spins[:50] = 1
    spins[50:] = 1
    #Perform Monte Carlo simulation
    energies,magnetisations=metropolis_monte_carlo(spins,J,h,T,num_steps,equ_steps)

    #Calculate average energy, average magnetization, susceptibility, and specific heat
    E_avg[i]=np.mean(energies[equ_steps:])
    M_avg[i]=np.mean(magnetisations[equ_steps:])
    X[i]=(1/T)*(np.mean(magnetisations[equ_steps:]**2)-M_avg[i]**2)
    C[i]=(1/T**2)*(np.mean(energies[equ_steps:]**2)-E_avg[i]**2)

#Plot the Graph 
plt.plot(T_range,E_avg)
plt.xlabel('Temperature (T)')
plt.ylabel('Average Energy')
plt.title('Average Energy vs Temperature')
plt.show()

plt.plot(T_range,M_avg)
plt.xlabel('Temperature (T)')
plt.ylabel('Average Magnetisation')
plt.title('Average Magnetisation vs Temperatur')
plt.show()

plt.plot(T_range,C)
plt.xlabel('Temperature (T)')
plt.ylabel('Specific Heat')
plt.title('Specific Heat vs Temperature')
plt.show()

plt.plot(T_range,X)
plt.xlabel('Temperature (T)')
plt.ylabel('Magnetic Susceptibility')
plt.title('Magnetic Susceptibility vs Temprature')

plt.show()
