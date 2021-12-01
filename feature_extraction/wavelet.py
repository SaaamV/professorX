import numpy as np
import pandas as pd
import pywt

data = pd.read_csv('data.csv')
sig = data['Af3']
dec=pywt.wavedec(sig, wavelet = 'db4', level=4)
