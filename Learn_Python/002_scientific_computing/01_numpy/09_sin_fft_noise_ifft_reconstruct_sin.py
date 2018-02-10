import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt

# frequency is the number of times a wave repeats a second
frequency = 1000
num_samples = 48000
# The sampling rate of the analog to digital convert
sampling_rate = 48000.0

#~ formula = sin(2*np.pi*freq*t)

tmp = [np.sin(2*np.pi*frequency*(x/sampling_rate)) for x in range(num_samples)]
tmp = np.array(tmp)

ax = plt.subplot(3,2,1)
plt.plot(tmp[:2000])
plt.subplot(3,2,2,sharex=ax)
fftdata = np.fft.fft(tmp)
frequencies = np.abs(fftdata)    
plt.plot(frequencies[:1005])

# Adding noise
# frequency is the number of times a wave repeats a second
noisy_frequency = 500
noisySin = [np.sin(2*np.pi*noisy_frequency*(x/sampling_rate)) for x in range(num_samples)]
noisySin = np.array(noisySin)
noisySin = noisySin+tmp
plt.subplot(3,2,3,sharex=ax)
plt.plot(noisySin[:2000])

# FFT of noisySin
noisy_fft = np.fft.fft(noisySin)
noisy_fft = np.abs(noisy_fft)    
plt.subplot(3,2,4,sharex=ax)
plt.plot(noisy_fft[:2000])


# Removing noise part from signal and plot the noise free signal
filtered_freq = []
index = 0
for f in noisy_fft:
    if index > 950 and index < 1050:
        if f >1:
            filtered_freq.append(f)
        else:
            filtered_freq.append(0)
    else:
        filtered_freq.append(0)
    index += 1

recovered_signal = np.fft.ifft(filtered_freq)
plt.subplot(3,2,5,sharex=ax)
plt.plot(recovered_signal[:2000])
plt.subplot(3,2,6,sharex=ax)
recovered_fft = np.fft.fft(recovered_signal)
plt.plot(abs(recovered_fft[0:2000]))
plt.show()