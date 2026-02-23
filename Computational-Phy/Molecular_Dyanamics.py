import random
import matplotlib.pyplot as plt
import numpy as np

# Lennard-Jones potential parameters
eps = 1.0 # Depth of the potential well
sig = 1.0 # Distance at which the potential is zero

# Simulation parameters
N = 100 # Number of particles
box_size = 15 # Size of the simulation box
dt = 0.01 # Time step
steps = 10000 # Number of simulation steps
m = 1.0 # Mass of each particle

# Function to initialize positions randomly inside the box
def init_position(N, box_size):
    positions = np.random.uniform(0, box_size, (N, 3)) # Generate N random positions in 3D
    return positions

# Function to initialize velocities to zero
def init_velocities(N):
    velocities = np.zeros((N, 3)) # Initialize velocities as a zero matrix
    return velocities

# Lennard-Jones potential function
def lj_potential(r, eps, sig):
    if r > 0:
        return 4 * eps * ((sig / r) ** 12 - (sig / r) ** 6) # Compute LJ potential
    else:
        return 0 # Return zero if distance is zero to avoid singularities

# Function to compute Lennard-Jones force
def lj_force(r_vec, eps, sig):
    r = np.linalg.norm(r_vec) # Compute the magnitude of the distance vector
    if r > 0:
        force_mag = 24 * eps * ((2 * (sig ** 12) / r ** 13) - (sig ** 6) / r ** 7) # Compute force magnitude
        return force_mag * (r_vec / r) # Compute force vector
    else:
        return np.zeros(3) # Return zero force if particles overlap

# Initialize positions and velocities
positions = init_position(N, box_size)
velocities = init_velocities(N)

# Lists to store energy values over time
pot_energies = []
kin_energies = []
total_energies = []

# Main simulation loop
for step in range(steps):
    PE = 0.0 # Initialize potential energy
    forces = np.zeros((N, 3)) # Initialize forces as zero for all particles

    # Compute forces and potential energy using pairwise interactions
    for i in range(N):
        for j in range(i + 1, N):
            r_vec = positions[i] - positions[j] # Compute distance vector
            F = lj_force(r_vec, eps, sig) # Compute force
            forces[i] += F # Apply force to particle i
            forces[j] -= F # Apply Newton's Third Law (equal & opposite force)
            r = np.linalg.norm(r_vec) # Compute distance
            PE += lj_potential(r, eps, sig) # Compute potential energy contribution

    # Velocity Verlet integration: First half update of velocity
    velocities += 0.5*(forces / m) * dt

    # Update positions
    positions += velocities * dt 

    # Compute new forces after position update
    new_forces = np.zeros((N, 3))
    for i in range(N):
        for j in range(i + 1, N):
            r_vec = positions[i] - positions[j] # Compute new distance vector
            F = lj_force(r_vec, eps, sig) # Compute force
            new_forces[i] += F # Apply force to particle i
            new_forces[j] -= F # Apply Newton's Third Law

    # Velocity Verlet integration: Second half update of velocity
    velocities += 0.5 * (new_forces / m) * dt

    # Compute kinetic energy
    KE = 0.5 * m * np.sum(velocities ** 2)

    # Store energy values
    pot_energies.append(PE)
    kin_energies.append(KE)
    total_energies.append(PE + KE)

# Convert energy lists to NumPy arrays
#pot_energies = np.array(pot_energies)
#kin_energies = np.array(kin_energies)
#total_energies = np.array(total_energies)

# Generate time steps for plotting
time_steps = np.arange(steps)

# Plot total energy over time to check energy conservation
plt.plot(time_steps, total_energies)
plt.plot(time_steps, kin_energies)
plt.plot(time_steps, pot_energies)
plt.xlabel("Time steps")
plt.ylabel("Total Energy")
plt.title("Molecular Dynamics Simulation")
plt.show()
