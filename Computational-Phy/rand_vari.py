#PROBABILITY DISTRIBUTIONS

import numpy as np
from scipy.stats import poisson, expon, norm, binom
import matplotlib.pyplot as plt 
import seaborn as sns

#Poisson distribution
lam = 5
poisson_rv = np.random.poisson(lam,1000)
print("Poisson Rv mean: ", np.mean(poisson_rv))
print("poisson Rv variancce: ", np.var(poisson_rv))

#Gaussian distribution
loc = 0
scale = 1
gaussian_rv = np.random.normal(loc, scale, 1000)
print("Gaussian Rv mean: ", np.mean(gaussian_rv))
print("Gaussian Rv variancce: ", np.var(gaussian_rv))

#Binomial distribution
n = 10
p = 0.5
binomial_rv = np.random.binomial(n, p ,1000)
print("Binomial Rv mean: ", np.mean(binomial_rv))
print("Binomial Rv variancce: ", np.var(binomial_rv))

#Exponential distribution
scale = 2
expo_rv = np.random.exponential(scale,1000)
print("exponential Rv mean: ", np.mean(expo_rv))
print("exponential Rv variancce: ", np.var(expo_rv))

#Plot the distributions
plt.figure(figsize=(14,6))

plt.subplot(2,2,1)
sns.histplot(poisson_rv, bins=20, kde=True)
plt.title("poisson distribution")
plt.xlabel("Value")
plt.ylabel("frequency")

plt.subplot(2,2,2)
sns.histplot(gaussian_rv, bins=20, kde=True)
plt.title("gaussian distribution")
plt.xlabel("Value")
plt.ylabel("frequency")

plt.subplot(2,2,3)
sns.histplot(binomial_rv, bins=20,kde=True)
plt.title("binomial distribution")
plt.xlabel("Value")
plt.ylabel("frequency")

plt.subplot(2,2,4)
sns.histplot(expo_rv, bins=20, kde=True)
plt.title("exponential distribution")
plt.xlabel("Value")
plt.ylabel("frequency")

plt.tight_layout()
plt.show()

""" 
OUTPUT:

Poisson Rv mean:  5.051
poisson Rv variancce:  5.000399
Gaussian Rv mean:  -0.019408323081537854
Gaussian Rv variancce:  1.0194021192134233
Binomial Rv mean:  4.97
Binomial Rv variancce:  2.4491
exponential Rv mean:  2.0177610680299516
exponential Rv variancce:  4.296133587586356
 """
