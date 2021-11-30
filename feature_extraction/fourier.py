import numpy as np
from scipy.fft import fft

sampling_freq = 128

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)

len_fft = y.size


# broken code
if y>=0.5 and y<=4:
    band = "D"
elif y>4 and y<=8:
    band = "T"
elif y>8 and y<=12:
    band = "A"
elif y>12 and y<=30:
    band = "B"
else:
    band= "useless"

print(band)