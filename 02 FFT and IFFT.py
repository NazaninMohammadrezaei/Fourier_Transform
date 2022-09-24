'''
_____________ Author _______________
Nazanin Mohammadrezaei
        
______________ COURSE ______________
Master the Fourier transform and its applications

______________ Topic _______________
FFT and IFFT using scipy library

____________ Instructor ____________
mikexcohen.com

'''

import numpy as np
import math
import matplotlib.pyplot as plt
import random
import timeit
import scipy.fftpack
from mpl_toolkits.mplot3d import Axes3D
get_ipython().run_line_magic('matplotlib', 'qt')


##################################### fft ########################################
# set parameters
srate = 1000
time  = np.arange(0,2,1/srate)
npnts = len(time)


# signal
signal = 2*np.sin(2*np.pi*6*time)


# Fourier spectrum
signalX = scipy.fftpack.fft(signal)/npnts
hz = np.linspace(0,srate/2,(np.floor(npnts/2)+1).astype(int))


# amplitude
amp = np.abs(signalX[0:len(hz)])
amp[1:] = 2*amp[1:]

plt.figure(1)
plt.stem(hz,amp,use_line_collection=True)
plt.xlim(0,10)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (a.u.)')
plt.show()


##################################### ifft ########################################
# set parameters
srate = 1000
time  = np.arange(0,3,1/srate)
pnts  = len(time)


# multispectral signal
signal  = np.multiply( (1+np.sin(2*np.pi*12*time)) , np.cos(np.sin(2*np.pi*25*time)+time) )


# fft
signalX = scipy.fftpack.fft(signal)


# reconstruction via ifft
reconSig = scipy.fftpack.ifft(signalX)

plt.figure(2)
plt.plot(time,signal,'r',label='Original')
plt.plot(time,np.real(reconSig),'--',label='Reconstructed')
plt.xlabel('Time (sec.)')
plt.ylabel('amplitude (a.u.)')
plt.legend(['Original','Reconstructed'])
plt.show()

