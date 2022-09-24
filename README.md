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
![Uploading Figure_2.png…]()

We also applied fft along the columns (over the time); Because the periodic waves are repeating over time ,we expect to see a meaningful amplitude spectrum.

