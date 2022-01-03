from PyQt6 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import pandas as pd
import scipy.fftpack
import sys  # We need sys so that we can pass argv to QApplication
import os

class PlotEEG(QtWidgets.QMainWindow):

    def __init__(self, channels, *args, **kwargs):
        super(PlotEEG, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)


        data = pd.read_csv("data1.csv")
        self.graphWidget.setBackground('w')
        self.graphWidget.setLabel('left', 'EEG Values')
        self.graphWidget.setLabel('bottom', 'Time Stamp')

        n = len(channels)
        dummy_var = 0
        self.graphWidget.addLegend()

        for i in channels:
            self.graphWidget.plot(data['Timestamp'], data[i], pen=(dummy_var,n), name = i[4:])
            dummy_var = dummy_var + 1

class PlotFFT(QtWidgets.QMainWindow):

    def __init__(self, channels, *args, **kwargs):
        super(PlotFFT, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)


        data = pd.read_csv("data1.csv")
        self.graphWidget.setBackground('w')
        

        N = int(len(data['EEG.AF3']))
        # number of samples
        T = 1.0/128.0
        # sample spacing
        

        n = len(channels)
        dummy_var = 0
        self.graphWidget.addLegend()
        for i in channels:
            y = np.array(data[i])
            X = np.fft.fft(y);
            f, y = self.dft_map(X, 128)


            self.graphWidget.plot(f, abs(y), pen=(dummy_var,n), name = i[4:])
            dummy_var = dummy_var + 1

    def dft_shift(self,X):
        N = len(X)
        if (N % 2 == 0):
            # even-length: return N+1 values
            return np.arange(-int(N/2), int(N/2) + 1), np.concatenate((X[int(N/2):], X[:int(N/2)+1]))
        else:
            # odd-length: return N values
            return np.arange(-int((N-1)/2), int((N-1)/2) + 1), np.concatenate((X[int((N+1)/2):], X[:int((N+1)/2)]))

    def dft_map(self, X, Fs, shift=True):
        resolution = float(Fs) / len(X)
        if shift:
            n, Y = self.dft_shift(X)
        else:
            Y = X
            n = np.arange(0, len(Y))
        f = n * resolution
        return f, Y