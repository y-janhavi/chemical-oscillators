import matplotlib.pyplot as plt
import numpy.random as rnd
import statistics as stat

# PARAMETERS
runs = 50  # Number of random walk simulations
trials = 50  # Number of steps per simulation
lattice_min = -10  # Minimum boundary of the lattice
lattice_max = 10   # Maximum boundary of the lattice
lattice_size = lattice_max - lattice_min + 1  # Total lattice points (201)

distances = []  # List to store final positions of each run

# SIMULATE RANDOM WALKS
for run in range(runs):
    position = 0  # Start at the origin
    path = [position]  # List to track movement over time

    for trial in range(trials):
        choice = rnd.rand()  # Generate random number between 0 and 1
        
        # Move left or right
        if choice < 0.5:
            position -= 1  # Move left
        else:
            position += 1  # Move right
        
        # Apply periodic boundary conditions
        if position > lattice_max:
            position = lattice_min  # Wrap around to the left
        elif position < lattice_min:
            position = lattice_max  # Wrap around to the right

        path.append(position)  # Record new position

    distance = path[-1]  # Final position after trials
    distances.append(distance)  # Store final position

    # Plot a single trajectory (only for the first run)
    if run == 0:
        plt.plot(path)
        plt.xlabel("Time")
        plt.ylabel("Position")
        plt.title("Single Trajectory of 1D Random Walk with Periodic Boundaries")
        plt.show()
    # Plot a Multiple trajectory 
    plt.plot(path)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Multiple Trajectory of 1D Random Walk with Periodic Boundaries")
plt.show()

# COMPUTE STATISTICS
mean_distance = stat.mean(distances)  # Mean final position
variance_distance = stat.variance(distances)  # Variance of final positions
stdev_distance = stat.stdev(distances)  # Standard deviation of final positions

# Print results
print(f"The mean end-to-end distance traveled is: {mean_distance}")
print(f"The standard deviation in the end-to-end distance traveled is: {stdev_distance}")
print(f"The variance in the end-to-end distance traveled is: {variance_distance}")

# PLOT HISTOGRAM OF FINAL POSITIONS
plt.hist(distances, bins=10, density=True)
plt.xlabel("End-to-End Distance")
plt.ylabel("Probability")
plt.title("Probability Distribution of 1D Random Walk with Periodic Boundaries")
plt.show()

"""
OUTPUT
--------------------------------------------------------------------------------
The mean end-to-end distance traveled is: 0.12
The standard deviation in the end-to-end distance traveled is: 5.759251652067023
The variance in the end-to-end distance traveled is: 33.16897959183674

"""