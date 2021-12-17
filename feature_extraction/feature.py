import numpy as np
import pandas as pd
from scipy import signal
from scipy.integrate import simps
import pywt

# must choose channel from 14 channels: AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4
class Feature():

    def __init__(self, filename = "data.csv"):
        # name of file where data is being stored along with extension
        self.filename = filename

    # function plots welchs periodogram and calculates area under the curve for respective frequency band using composite simpsons rules
    def relative_psd(self, channel):
        fs = 128
        t = 3
        # t is the duration of the signal, this value must be same is record.py and stimuli/cues.py as well

        N = fs * t

        win_length = 4*fs
        # window length is normally 2/Lowest freq of interest which is 0.5 in our case thus the window length is 4 seconds

        data = pd.read_csv(self.filename)

        freqs, psd = signal.welch(data[channel], fs, nperseg=win_length)

        """
        plt.plot(freqs, psd, color='k', lw=2)
        plt.xlabel('Frequency')
        plt.ylabel('Power spectral density')
        plt.title("Welch's periodogram")
        """

        # delta band 
        low = 0.5
        high = 4
        delta = np.logical_and(freqs >= low, freqs <= high)
        freq_res = freqs[1] - freqs[0] 
        delta_power = simps(psd[delta], dx=freq_res)

        total_power = simps(psd, dx=freq_res)

        delta_rel_power = delta_power / total_power
        #print('relative delta power = %.3f '% delta_rel_power)

        # theta band 
        low = 4
        high = 8
        theta = np.logical_and(freqs >= low, freqs <= high)
        freq_res = freqs[1] - freqs[0] 
        theta_power = simps(psd[theta], dx=freq_res)
        theta_rel_power = theta_power / total_power
        #print('relative theta power = %.3f '% theta_rel_power)

        # alpha band 
        low = 8
        high = 12
        alpha = np.logical_and(freqs >= low, freqs <= high)
        freq_res = freqs[1] - freqs[0] 
        alpha_power = simps(psd[alpha], dx=freq_res)
        alpha_rel_power = alpha_power / total_power
        #print('relative alpha power = %.3f '% alpha_rel_power)

        # beta band 
        low = 12
        high = 30
        beta = np.logical_and(freqs >= low, freqs <= high)
        freq_res = freqs[1] - freqs[0] 
        beta_power = simps(psd[beta], dx=freq_res)
        beta_rel_power = beta_power / total_power
        #print('relative beta power = %.3f '% beta_rel_power)

        """
        powers = [delta_rel_power, theta_rel_power, alpha_rel_power, beta_rel_power]
        """
    def wavelet(self, channel):
        data = pd.read_csv(self.filename)
        sig = data[channel]
        dec=pywt.wavedec(sig, wavelet = 'db4', level=4)
    
