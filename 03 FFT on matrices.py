'''
_____________ Author _______________
Nazanin Mohammadrezaei
        
______________ COURSE ______________
Master the Fourier transform and its applications

______________ Topic _______________
Using FFT on matrices

____________ Instructor ____________
mikexcohen.com

'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import numpy.matlib
get_ipython().run_line_magic('matplotlib', 'qt')


# generate multivariate dataset
srate = 400
time  = np.arange(0,srate*2)/srate
npnts = len(time)
nreps = 50


# dataset is repeated sine waves
data = np.matlib.repmat( np.sin(2*np.pi*10*time), nreps,1 )


# FFT of data along each dimension
dataX1 = scipy.fftpack.fft(data,axis=0) / npnts
dataX2 = scipy.fftpack.fft(data,axis=1) / npnts
hz = np.linspace(0,srate/2,int(np.floor(npnts/2)+1))


# check sizes
print('fft over channels is of size = ',np.shape(dataX1))
print('fft over time is of size = ',np.shape(dataX2))


# show data and spectra
plt.figure(1)
plt.imshow(data)
plt.xlabel('Time')
plt.ylabel('Channel')
plt.title('Time-domain signal')
plt.show()

plt.figure(2)
plt.stem(hz,np.mean(2*abs(dataX1[:,:len(hz)]),axis=0),'k',use_line_collection=True)
plt.xlabel('Frequency (??)')
plt.ylabel('Amplitude')
plt.title('FFT over channels')
plt.show()

plt.figure(3)
plt.stem(hz,np.mean(2*abs(dataX2[:,:len(hz)]),axis=0),'k',use_line_collection=True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT over time')
plt.show()

