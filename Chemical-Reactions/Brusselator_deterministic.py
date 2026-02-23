#DETERMINISTIC SIMULATION OF COUPLED CHEMICAL REACTION - BRUSSELATOR REACTION MODEL
 
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Reactions
# X-----> Y1 with c1
# X2 + Y1 ------> Y2 + Z1 with c2
# 2Y1 + Y2 -----> 3Y1 with c3
# Y1 ----> Z2 with c4

#Define the system of differential equations
def equations(t,y):
    k1, k2, k3, k4 = 5000, 50, 0.00005, 5 #Parameters
    y1, y2 = y #Unpack the current state
    dy1dt = k1 - k2*y1 + k3*y1*y1*y2/2 - k4*y1 #Derivative of Y1
    dy2dt = k2*y1 - k3*y2*y1*y1/2 #Derivative of Y2
    return(dy1dt,dy2dt)

#Initial conditions
y0 = [0.13706323027549128, 0.4682405161100677]

#Time parameters
T = 10.0
time_span = (0,T)
time_eval = np.arange(0,T,0.001)

#Solve differential equations
sol = solve_ivp(equations, time_span, y0, method= 'RK45', t_eval=time_eval)

#Extract the solutions
y1t = sol.y[0]
y2t = sol.y[1]
time = sol.t

#Plot the results
plt.figure()
plt.plot(time, y1t, label ='Y1')
plt.plot(time, y2t, label ='Y2')
plt.xlabel('time')
plt.ylabel('population')
plt.title('Brusselator model')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.legend(loc = 'upper right')
plt.show()

#Phase Plot
plt.figure()
plt.plot(y1t,y2t)
plt.xlabel('Number of Y1 molecule')
plt.ylabel('Number of Y2 molecule')
plt.title('Brusselator model')
plt.xlim(left = 0)
plt.ylim(bottom =0)
plt.show()
