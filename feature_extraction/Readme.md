# Code for feature extraction from raw eeg signal

### Pre-requisites
pip install numpy
pip install PyWavelets

## Background
The eeg signal from each channel can be categorised into one of four frequency bands,
1. Delta [0.5-4 hz]
2. Theta [4-8 hz]
3. Alpha [8-12 hz]
4. Beta [12-30 hz]

## fourier.py
Applies fourier transform on channel data.

## psd.py
Uses the welsch periodogram function to calculate the power spectral density for a particular channel and then relative band power for each of four frequency bands.

## wavelet.py
Frequency-time analysis using wavelet-transform.




