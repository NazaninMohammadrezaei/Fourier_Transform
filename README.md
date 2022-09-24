# Fourier Transform
In this repository, I gather the materials about fourier transform which I have learned from the udemy course `Master the Fourier transform and its applications` by `Dr. Mike X. Cohen`. I actually focused not only on the libraries that contribute to simply use fourier transform, but also on implementing it totally from the ground up without using the specific libraries in order to understand the mathematical basis of every line of code. 

Make sure to visit Dr. Cohen's website: [www.mikexcohen.com](https://www.mikexcohen.com/)

And here is the link to this course: [Course Link](https://www.udemy.com/course/fourier-transform-mxc/)
<br><br>

Also file names are representative of their content , but here is an explanation for each of them:

`01 DTFT` : Implementing Discrete Time Fourier Transform from the scratch, without specific libraries

`02 FFT and IFFT` : Implementing Discrete Time Fourier Transform and its inverse, using fft and ifft, provided in the scipy library

`03 FFT on matrices` : Using fft on 2d arrays
<br><br>

## Discrete Time Fourier Transform
An step-by-step process to apply fourier transform on a sample signal: 2.5sin(2π4) + 1.5sin(2π6.5)

![Figure_1](https://user-images.githubusercontent.com/88426435/192046683-7eecbdba-561a-45de-a534-c94c0dee0231.png)
<br>

## FFT and IFFT
The fft of a simple sine wave: 2sine(2π6) 

![02_1](https://user-images.githubusercontent.com/88426435/192085215-66126821-d367-471e-808d-f67b9b29bfe7.png)

Then, we generated a multivariate signal, applied fft on the signal, and reconstructed it using ifft.

![02_2](https://user-images.githubusercontent.com/88426435/192085495-65e754dc-2d58-41ac-badc-9b88f6763a75.png)

## FFT on matrices
The data is a 2d repeating sine wave.

![Figure_1](https://user-images.githubusercontent.com/88426435/192085544-5180b499-1e42-4fb2-9459-fa502f26799b.png)

We applied fft along the rows (over the channels); Because the periodic waves are repeating over time and not channels ,we expect not to see a meaningful diagram.

![Figure_2](https://user-images.githubusercontent.com/88426435/192085769-f3da5320-5072-4f32-9379-6cba22b7d14f.png)

We also applied fft along the columns (over the time); Because the periodic waves are repeating over time ,we expect to see a meaningful amplitude spectrum.

![Figure_3](https://user-images.githubusercontent.com/88426435/192085775-586118d1-4880-4c66-8a5f-184b056a79a6.png)

## Frequency resolution and Zero-padding

Here, we manually added zeros to the end of our signal. In this figure, we can see how zero-padding in the time domain affects the frequency domain.

![Figure_1](https://user-images.githubusercontent.com/88426435/192090120-aa6d0eca-2f83-404b-929e-7ee770457527.png)

Here, we see how zero-padding in the time domain using the fft command (not manually) affects the amplitude spectrum of the signal.

![TDZP_nonmanual](https://user-images.githubusercontent.com/88426435/192090128-d53ff242-51cd-4242-90b2-62b391208a7d.png)

And here, we see how zeropadding in the frequency domain, affects the reconstructed signal.

![fDZP_nonmanual](https://user-images.githubusercontent.com/88426435/192090133-17f471d9-3ba0-4977-8912-e16bc9a93d78.png)

## Aliasing

The original signal is a sine wave with 10 Hz frequency. 
Aliasing happened when sampling frequency was lower that nyquist rate of the signal. (which is 2*10)
Theoritically, a sampling frequency of `2*the higher bound of signal` is enough, but practically, sampling frequencies of around `5*the higher bound of signal` are much more approriate.

![aliasing](https://user-images.githubusercontent.com/88426435/192090153-5e1f04a9-e84c-447e-88fb-f51beaba48e0.png)


## Application 1: The rythmicity of EEG data

For this brain signal, two peaks are witnessed at 10 Hz (related to brain alpha waves), and 50 Hz (related to power supply noise)

![untitled3](https://user-images.githubusercontent.com/88426435/192090329-9c3ffb7a-6e1b-4fa7-86ee-dcbee224c238.png)


## Application 2: Low Pass Filtering an image

Applying a gaussian low pass filter makes the image smoother.

![untitled2](https://user-images.githubusercontent.com/88426435/192090335-9e17eeee-d0c6-4670-a41b-57567b99860b.png)


## Application 3: Filtering an image composed of two sine wave gradients

The image is composed of two sine waves with a 45 degree phase difference. I applied frequency-domain filtering on the image by excluding the parts of amplitude spectrum which corresponds to the first sine wave. Afterwards, we get a filtered image which is only contains a sine wave with a phase of 45 degrees. It's like we removed the first wave gradient from the image.

![untitled](https://user-images.githubusercontent.com/88426435/192090342-639c7a4b-5d5c-4f6f-8c98-891a724214ce.png)
