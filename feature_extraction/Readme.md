# Code for feature extraction from raw eeg signal

## bands.py
Divides the eeg signal from each channel into one of four frequency bands,
1. Delta [0.5-4 hz]
2. Theta [4-8 hz]
3. Alpha [8-12 hz]
4. Beta [12-30 hz]

## psd.py
Uses the autocorrelation function to calculate the power spectral density for a particular channel


