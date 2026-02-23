import numpy as np
import matplotlib.pyplot as plt

# Parameters
grid_size = 10  # Defines the boundary limits (-grid_size to +grid_size)
steps = 1000  # Number of steps

# Initialize walker at the origin
x, y = 0, 0

# Store walk history
x_pos_list = [x]
y_pos_list = [y]

# Random Walk with Periodic Boundaries
for _ in range(steps):
    direction = np.random.choice(["up", "down", "left", "right"])
   
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
   
    # Apply periodic boundary conditions
    if x > grid_size:
        x = -grid_size
    elif x < -grid_size:
        x = grid_size
   
    if y > grid_size:
        y = -grid_size
    elif y < -grid_size:
        y = grid_size

    x_pos_list.append(x)
    y_pos_list.append(y)

# Plot the walk
plt.figure(figsize=(6, 6))
plt.plot(x_pos_list, y_pos_list, marker=".", linestyle="-", alpha=0.6)
plt.scatter(0, 0, color="blue", label="Start", zorder=3)  # Start position
plt.scatter(x, y, color="red", label="End", zorder=3)  # End position
plt.grid()
plt.legend()
plt.title("2D Random Walk with Periodic Boundaries")
plt.show()