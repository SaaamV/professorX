import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

fs = 128
t = 3
# t is the duration of the signal, this value must be same is record.py and stimuli/cues.py as well

N = fs * t

win_length = 4*fs
# window length is normally 2/Lowest freq of interest which is 0.5 in our case which is 4 seconds

data = pd.read_csv('data.csv')

freqs, psd = signal.welch(data['Af3'], fs, nperseg=win_length)
plt.plot(freqs, psd, color='k', lw=2)
plt.xlabel('Frequency')
plt.ylabel('Power spectral density')
plt.title("Welch's periodogram")


