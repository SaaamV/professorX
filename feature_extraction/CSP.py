import numpy as np
import scipy.signal

class Csp():
    def __init__(self, channels):
        self.channels = channels

    def band_pass(self, low, high, order):
        