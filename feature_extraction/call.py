from feature import Feature
import numpy as np
import pandas as pd

Channels = ['EEG.AF3', 'EEG.F7', 'EEG.F3','EEG.FC5','EEG.T7','EEG.P7','EEG.O1','EEG.O2','EEG.P8','EEG.T8','EEG.FC6','EEG.F4','EEG.F8','EEG.AF4']

psd = Feature('right.csv')
for channel in Channels:
    psd.psd(channel)