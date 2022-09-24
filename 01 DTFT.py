'''
_____________ Author _______________
Nazanin Mohammadrezaei
        
______________ COURSE ______________
Master the Fourier transform and its applications

______________ Topic _______________
Implementing Discrete Time Fourier Transform from the ground up

____________ Instructor ____________
mikexcohen.com

'''

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.fftpack
import random
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', 'qt')


# create the signal
srate = 1000
time = np.arange(0,2,1/srate)
signalpoints = len(time)
signal = 2.5 * np.sin( 2 * np.pi * 4 * time ) + 1.5 * np.sin( 2 * np.pi * 6.5 * time )


# prepare the fourier transform
Fourtime = np.array(range(signalpoints)) / signalpoints
fcoef = np.zeros((len(signal)),dtype = complex)


# fourier transform
for fi in range(signalpoints):
    csw = np.exp(-1j * 2 * np.pi * fi * Fourtime)
    fcoef[fi] = np.sum(np.multiply(csw,signal)) / signalpoints

    
# amplitude spectrum
amp = np.abs(fcoef)
amp[1:] = 2*amp[1:]


# check whether the length of signal is even or odd to determine the top frequencywe can plot
if signalpoints%2 == 0:
    topfreq = srate/2
elif signalpoints%2 == 1:
    topfreq = (srate/2) * (signalpoints-1/signalpoints)

    
# x axis (frequency) of the diagram
hz = np.linspace(0,topfreq,np.floor(signalpoints/2.+1).astype(int))


# plot amlitude spectrum of our signal
plt.figure(1)
plt.stem(hz,amp[range(len(hz))], use_line_collection=True)
plt.xlabel('Frequency (Hz)'), plt.ylabel('Amplitude (a.u.)')
plt.xlim(0,10)
plt.title('Discrete Time Fourier Transform')
plt.show()

