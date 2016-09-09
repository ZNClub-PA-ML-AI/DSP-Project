# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:15:24 2016

@author: Nevil Dsouza
"""
import wave
#print("import success")

### method to compute absolute value of vector
def absolute_value_of_vector(vector):
    print("inside f(x)")
    return []
    
### method to compute FFT
def fft(x):
    print("inside f(x)")
    return []

### method to recognize a YES or a NO from wav sample
def recognize_yes_or_no(N,fs,wav):
    print("inside f(x)")
    print("N=",N," fs=",fs)
    # threshold frequency
    F=12    
    
    # length of samples
    k1=round(N*5000/fs)
    k2=round(N*11025/fs)
    
    print("values of k1,k2 are:",k1,k2)
    
    X=absolute_value_of_vector(fft(wav))
    
    #f=sum(X[1:k1])/sum(X[k1:k2])
    f=10
    
    if f<F:
        print("IVR RESPONSE = YES")
    else:
        print("IVR RESPONSE = NO")        
    return

### read a wav file
with wave.open("test1.wav", mode='rb') as wav:
    print("read success")
#    
#    # does not work
#    print(wav)
#    
#    print("Returns number of audio channels (1 for mono, 2 for stereo).\n",wav.getnchannels())
#    
#    print("Returns sample width in bytes.\n",wav.getsampwidth())
#    
#    print("Returns sampling frequency.\n",wav.getframerate())
#
#    print("Returns number of audio frames.\n",wav.getnframes())
#    
#    print("Returns compression type \n",wav.getcomptype(),wav.getcompname())    
#
#    print("Returns a namedtuple() (nchannels, sampwidth, framerate, nframes, comptype, compname), equivalent to output of the get*() methods\n",wav.getparams())    
#    
    recognize_yes_or_no(wav.getnframes(),wav.getframerate(),wav)    
    
    wav.close()
    print("close success")
    
    