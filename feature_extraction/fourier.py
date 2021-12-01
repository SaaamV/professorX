import numpy as np
import pandas as pd
from scipy.fft import fft
import matplotlib.pyplot as plt


data = pd.read_csv()
y = fft(data['Af3'])

#plt.plot(abs(y))
#plt.show