% _________Author_________
% Nazanin Mohammadrezaei

% _________COURSE_________
% Master the Fourier transform and its applications

% _________Topic__________
% Applications of the Fourier transform - Image narrowband filtering

% _______Instructor_______
% mikexcohen.com

%% Filter a combination of two sine wave gradients to reconstruct one of them

% specify sine waves' phases
sinephas = [ 0 pi/4 ];

% specify sine waves' frequencies
sinefreq = [.1 .05];  % arbitrary units

% sine wave initializations
lims  = [-91 91];
[x,y] = ndgrid(lims(1):lims(2),lims(1):lims(2));

% compute 2D sine gradients
xp = x*cos(sinephas(1)) + y*sin(sinephas(1));
img1 = sin( 2*pi*sinefreq(1)*xp );

xp = x*cos(sinephas(2)) + y*sin(sinephas(2));
img2 = sin( 2*pi*sinefreq(2)*xp );

% combine images
img = img1+img2;



figure(1), clf

% show original two gradients
subplot(321)
imagesc(img1), axis off, axis square
title('One image')

subplot(322)
imagesc(img2), axis off, axis square
title('Second image')

% show sum of the two gradients
subplot(323)
imagesc(img), axis off, axis square
title('Summed image')

% FFT
imgX    = fftshift(fft2(img));
imgXamp = abs(imgX);

% show amplitude spectrum
subplot(324)
imagesc(imgXamp)
set(gca,'clim',[0 500])
axis off, axis square
title('Amplitude spectrum')

% show sum down the columns
subplot(325)
stem(sum(imgXamp),'ks'), axis square
title('Column sum of power spectra')

% exclude sine wave with phase zero from the image
imgX(:,1) = imgX(:,end);

% reconstructed image
imgrecon  = real(ifft2(fftshift(imgX)));

% expecting to see a sine with phase 45, 
% after filtering the sine with phase 0
subplot(326)
imagesc(imgrecon), axis square, axis off
title('Filtered image')

