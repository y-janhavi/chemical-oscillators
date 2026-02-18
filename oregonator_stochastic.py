# STOCHASTIC SIMULATION OF COUPLED CHEMICAL REACTION - OREGONATOR REACTION MODEL 
 
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Reactions
# X1 + Y2 ------> Y1 with reaction rate c1
# Y1 + Y2 ------> Z1 with reaction rate c2
# X2 + Y1 ------> 2Y1 + Y3 with reaction rate c3
# 2Y1 ------> Z2 with reaction rate c4
# X3 + Y3 ------> Y2 with reaction rate c5

#Define initial conditions
Y1 = 500
Y2 = 1000
Y3 = 2000

#Define reaction rates
c1X1, c2, c3X2, c4, c5X3 = 2, 0.1, 104, 0.016, 26

#Define time parameters
t = 0
finalt = 6

#Initialize array to store values
tp = [0]
Y1_v = [Y1]
Y2_v = [Y2]
Y3_v = [Y3]

#Simulate the reactions using gillespie algorithm
while t < finalt and (Y1>0 or Y2>0 or Y3>0):
    #Calculate propensity function for each reaction
    a1 = c1X1*Y2
    a2 = c2*Y1*Y2
    a3 = c3X2*Y1
    a4 = c4*Y1*(Y1-1)/2
    a5 = c5X3*Y3
    #calculate total propensity function
    ao = a1+a2+a3+a4+a5

    r1 = random.uniform(0,1) #Generate a random number for choosing step step

    #Update time steps
    if ao > 0:
        '''tau = (1/ao)*math.log(1/r1)'''
    else:
        tau = float('int')
    t = t+tau

    r2 = random.uniform(0,1) #Generate a random number for choosing the reaction

    #Update the populations based on the reactions
    if ao*r2 < a1:
        Y1 += 1
        Y2 = Y2 - 1
    elif ao*r2 < a1+a2:
        Y1 = Y1 - 1
        Y2 = Y2 - 1
    '''elif ao*r2 < a1+a2+a3:
        Y1 = Y1 + 1 
        Y3 = Y3 + 1
    elif ao*r2 < a1+a2+a3+a4:
        Y1 = Y1 - 2'''
    elif ao*r2 < a1+a2+a3+a4+a5:
        Y2 = Y2 + 1 
        Y3 = Y3 - 1

    #Append the values
    tp.append(t)
    Y1_v.append(Y1)
    Y2_v.append(Y2)
    Y3_v.append(Y3)

#Plot the results    
plt.plot(tp,Y1_v,label='Y1 molecule')
plt.plot(tp,Y2_v,label='Y2 molecule')
plt.plot(tp,Y3_v,label='Y3 molecule')
plt.xlabel('Time (t)')
plt.ylabel('Number of Y1,Y2 and Y3 molecules')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.title('Oregonator model')
plt.legend(loc = 'upper right')
plt.show()

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(Y1_v,Y2_v,Y3_v,'hotpink')
ax.set_xlabel('number of Y1 molecules', fontsize = 6)
ax.set_ylabel('number of Y2 molecules', fontsize = 6)
ax.set_zlabel('number of Y3 molecules', fontsize = 6)
ax.set_title('Oregonator model')
plt.show()