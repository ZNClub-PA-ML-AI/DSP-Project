# DSP-Project
- Speech Recognition for IVRS  based upon predefined grammars used in "directed" dialogues 
- Speech to Text conversion of recorded response

## Speech Recognition for IVRS  based upon predefined grammars used in "directed" dialogues 

### Concept

1. The idea is to recognize response of a customer during an IVRS session based on the keywords "yes" and "no".
2. The power spectral density, which is based on the FFT, is a plot of the estimated spectrum of a signal. If the power spectral density of a recording of a person saying yes is compared to that of no, usually the spectrum of yes has more energy in the high frequencies because of the “s” sound in yes.

### Algorithm for Speech Recognition

1. Divide input files into 2:
  1. Training Set
  2. Testing Set
2. 
. Feature to be used is the ratio of A to B where:
    A: sum of the magnitude of the FFT components that correspond to the low frequencies
    B: sum of the magnitude of the FFT components that correspond to the high frequencies
    i.e.  f = A/B

