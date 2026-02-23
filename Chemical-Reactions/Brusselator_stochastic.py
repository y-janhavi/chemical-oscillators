#STOCHASTIC SIMULATION OF COUPLED CHEMICAL REACTIONS - BRUSSELATOR REACTION MODEL
 
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Reactions
# X-----> Y1 with c1
# X2 + Y1 ------> Y2 + Z1 with c2
# 2Y1 + Y2 -----> 3Y1 with c3
# Y1 ----> Z2 with c4

#Define initial conditions
Y1 = 1000
Y2 = 2000

#Define reaction rates
c1X, c2X2, c3, c4 = 5000, 50, 0.00005, 5

#Define time parameters
t = 0
finalt = 10

#Initialize array to store values
tp = [0]
Y1_v = [Y1]
Y2_v = [Y2]

#Simulate the reactions
while t < finalt and (Y1>0 or Y2>0):
    #Calculate propensity function for each reaction
    a1 = c1X
    a2 = c2X2*Y1
    a3 = c3*Y2*Y1*(Y1-1)/2
    a4 = c4*Y1
    #calculate total propensity function
    ao = a1+a2+a3+a4

    r1 = random.uniform(0,1) #Generate a random number for choosing time step

    #Update time steps
    if ao > 0:
        tau = (1/ao)*math.log(1/r1)
    else:
        tau = float('int')
    t = t+tau

    r2 = random.uniform(0,1) #Generate a random number for choosing reactions

    #Update the populations based on the reactions
    if ao*r2 < a1:
        Y1 += 1
    elif ao*r2 < a1+a2:
        Y2 = Y2 + 1
        Y1 = Y1 - 1
    elif ao*r2 < a1+a2+a3:
        Y2 = Y2 - 1
        Y1 = Y1 + 1
    elif ao*r2 < a1+a2+a3+a4:
        Y1 = Y1 - 1    

    #Append the values
    tp.append(t)
    Y1_v.append(Y1)
    Y2_v.append(Y2)

#Plot the reults   
plt.plot(tp,Y1_v,label='Y1 molecule')
plt.plot(tp,Y2_v,label='Y2 molecule')
plt.xlabel('Time (t)')
plt.ylabel('Number of Y1 and Y2 molecules')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.title('Brusselator model')
plt.legend()
plt.show()

plt.plot(Y1_v,Y2_v)
plt.xlabel('Number of Y1 molecules')
plt.ylabel('Number of Y2 molecules')
plt.title('Brusselator model')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.legend()
plt.show()
