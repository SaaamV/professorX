import math
import numpy as np
from scipy.fft import fft

N = length(x)
xdft = fft(x)
psdx = (1/(2*math.pi*N)) * abs(xdft)**2




# Alternate code using welsh's periodogram 
