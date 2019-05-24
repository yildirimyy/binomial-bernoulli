# Binomial Dist

from scipy.stats import binom
import matplotlib.pyplot as plt
   
fig, ax = plt.subplots(1, 1)
x = range(7)
n, p = 6, 0.5
rv = binom(n, p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,label='Probablity of Success')          
ax.legend(loc='best', frameon=False)          
plt.show()

# Std

import statistics 
  
# creating a simple data - set 
sample = [11, 21, 78, 3, 64] 
  
# Prints standard deviation 
# xbar is set to default value of 1 
print("Standard Deviation of sample is % s " 
                % (statistics.stdev(sample))) 




