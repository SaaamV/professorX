
import numpy as np
# total number of elements
n = 120
# k is the number of zeros
k = 60
arr = np.array([0]*k + [1]*(n-k))
np.random.shuffle(arr)


