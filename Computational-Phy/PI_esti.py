# ESTIMATION OF PI VALUE USING MONTE CARLO METHOD

import random
import math
import matplotlib.pyplot as plt

# Define a list of different number of runs to test the simulation
num_list = [100,500,1000,5000,10000,50000,100000,200000,400000,600000,1000000]
pi_esti = []

# Run the simulation for each number of runs
for num in num_list:
    # Initialize a counter for the number of points inside the circle
    in_circle = 0

    # Initialize a counter for the number of points inside the square
    in_square = 0

    # Run the simulation for the specified number of runs
    for n in range(num):
        # Generate random x and y coordinates betweenn -1 and 1
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        # Check if the point is inside the unit circle(distance <=1)
        if x**2 + y**2 <= 1:
            # Increament the counter if the point is inside the circle
            in_circle += 1
        in_square +=1

        # Calculate the estimated Pi value using Monte Carlo method
        pi_estimate = 4*in_circle/in_square
    pi_esti.append(pi_estimate)

# Print the estimated Pi value and the absolute error
print("No. of points\testimated PI value\tactual PI value\n---------------------------------------------------------------------")
for i in range (len(num_list)):
    print(f"{num_list[i]}\t\t\t\t{pi_esti[i]}\t\t\t\t{math.pi}")

'''
OUTPUT

No. of points	  estimated PI value	 actual PI value
------------------------------------------------------------
100				    2.96				3.141592653589793
500				    3.088				3.141592653589793
1000				3.116				3.141592653589793
5000				3.1464				3.141592653589793
10000				3.1536				3.141592653589793
50000				3.13064				3.141592653589793
100000				3.15132				3.141592653589793
''' """

 """