# DSP-Project
- Speech Recognition for IVRS  based upon predefined grammars used in "directed" dialogues 
- Speech to Text conversion of recorded response

## Speech Recognition for IVRS  based upon predefined grammars used in "directed" dialogues 

### Concept

1. The idea is to recognize response of a customer during an IVRS session based on the keywords "yes" and "no".
2. The power spectral density, which is based on the FFT, is a plot of the estimated spectrum of a signal. If the power spectral density of a recording of a person saying yes is compared to that of no, usually the spectrum of yes has more energy in the high frequencies because of the “s” sound in yes.
3. Assumptions based on Research Paper Experiment Observations:
  1. feature is the sum of magnitude of the FFT values for the frequencies 0 to 5000 Hz divided by
sum of magnitude of the FFT values from 5000 to 11025 Hz, which is the highest frequency for
the training files because their sampling rate is 22050 Hz.
  2. Threshold value of 12 separates most of the yes and no values.
  
### Algorithm for Speech Recognition

1. Divide input files into 2:
  1. Training Set
  2. Testing Set
2. Calculate the feature for all of the training files and examine the histogram for the yes values and the no values.
3. Select a threshold frequency F which separates the "yes" samples & the "no" samples.
3. For any sample in Testing Set:
  Feature to be used is the ratio of A to B where:
    A: sum of the magnitude of the FFT components that correspond to the low frequencies
    B: sum of the magnitude of the FFT components that correspond to the high frequencies
    i.e.  
    f = A/B
    
    if f < F:
      sample belongs to "yes" cluster
    else:
      sample belongs to "no" cluster
    
### General Information

1. WAV Files : high quality, huge size, stored in binary
2. .OPUS Files: .OGG format used by Whatsapp Inc to store Voice Notes. This was done to overcome platform specific issues faced by AAC and AMR formats
3. DFT is mathematical idea which takes a signal and produces its spectrum. The spectrum is the set of sinusoids that add up to produce the signal.
4. FFT is an algorithm which is an efficient way to compute the DFT.
5. An audio frame, or sample, contains amplitude (loudness) information at that particular point in time.

### Code in Research Paper

    function output = yes_no(x,fs)
    % function output = yes_no(x,fs)
    % Simple algorithm for deciding whether the audio signal
    % in vector x is the word 'yes' or 'no'.
    % x (vector) speech signal
    % fs (scalar) sampling frequency in Hz
    % output (string) 'yes' or 'no'
    threshold = 12; % threshold value
    N = length(x);
    k1 = round(N*5000/fs); % FFT component corresponding to 5000 Hz
    k2 = round(N*11025/fs); % FFT component corresponding to 11025 Hz
    X = abs(fft(x));
    f = sum(X(1:k1))/sum(X(k1:k2)); % calculate feature
    if f < threshold,
     output = 'yes'; % if feature is below threshold, return 'yes'
    else
     output = 'no'; % if feature is above threshold, return 'no'
