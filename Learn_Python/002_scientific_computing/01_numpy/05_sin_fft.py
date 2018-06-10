"""
Author : Pankaj soni
"""


import numpy as np
import matplotlib.pyplot as plt

Fs = 500.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,1,Ts) # time vector

ff = 20;   # frequency of the signal
y = np.sin(2*np.pi*ff*t)

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
#~ print frq
frq = frq[range(n/2)] # one side frequency range
#~ print frq
Y = np.fft.fft(y)/n # fft computing and normalization
#~ print Y
Y = Y[range(n/2)]
#~ print Y

fig,tmp = plt.subplots(2,1)
tmp[0].plot(y)
tmp[1].plot(abs(Y))

plt.show()
