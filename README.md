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
    
