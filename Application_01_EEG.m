% _________Author_________
% Nazanin Mohammadrezaei

% _________COURSE_________
% Master the Fourier transform and its applications

% _________Topic__________
% Applications of the Fourier transform - Rythmicity in EEG

% _______Instructor_______
% mikexcohen.com

%% FFT of a brain wave

load EEGrestingState.mat

n = length(eegdata);
timevec = (0:n-1)/srate;

% compute amplitude spectrum
dataX    = fft(eegdata)/n;
ampspect = 2*abs(dataX);
hz       = linspace(0,srate/2,floor(n/2)+1);


figure(1), clf

% plot time domain signal
subplot(211)
plot(timevec,eegdata,'k')
xlabel('Time (sec.)'), ylabel('Amplitude (\muV)')
title('Time domain signal')

subplot(212)
plot(hz,smooth(ampspect(1:length(hz)),30),'r','linew',2)
set(gca,'xlim',[0 70],'ylim',[0 .6])
xlabel('Frequency (Hz)'), ylabel('Amplitude (\muV)')
title('Frequency domain')



