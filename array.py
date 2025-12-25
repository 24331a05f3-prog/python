import numpy as np
temps=[25,34,26,29,28,37,32]
print("given list is: ",temps)
temp =np.array(temps)
print("np array: ",temp)
print("Number of dimensions:", temp.ndim)
print("Maximum temperature:", np.max(temp))
print("Minimum temperature:", np.min(temp))
print("Mean temperature:", np.mean(temp))
print("Variance:", np.var(temp))
print("Standard Deviation:", np.std(temp))