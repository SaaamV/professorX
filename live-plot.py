import matplotlib.pyplot as plt
import numpy as np
import collections
channel1 = collections.deque(np.zeros(10))
channel2 = collections.deque(np.zeros(10))
channel3 = collections.deque(np.zeros(10))
channel4 = collections.deque(np.zeros(10))
channel5 = collections.deque(np.zeros(10))
channel6 = collections.deque(np.zeros(10))
channel7 = collections.deque(np.zeros(10))
channel8 = collections.deque(np.zeros(10))
channel9 = collections.deque(np.zeros(10))
channel10 = collections.deque(np.zeros(10))
channel11 = collections.deque(np.zeros(10))
channel12 = collections.deque(np.zeros(10))
channel13 = collections.deque(np.zeros(10))
channel14 = collections.deque(np.zeros(10))

eeg_dict = {1:channel1,
2:channel2,
3:channel3,
4:channel4,
5:channel5,
6:channel6,
7:channel7,
8:channel8,
9:channel9,
10:channel10,
11:channel11,
12:channel12,
13:channel13,
14:channel14,
}


def update_data():
    for i in range(1,15):
        # getting data
        eeg_dict[i].popleft()
        eeg_dict[i].append()

    # plotting the data
    fig, ax = plt.subplots(14, 1,squeeze=False)
    for i in range(1,15):
        ax[i-1][0].plot(eeg_dict[i])
    # clearing the axis
    ax.cla()