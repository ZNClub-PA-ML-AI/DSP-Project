# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:15:24 2016

@author: Nevil Dsouza
"""
import wave
from scipy.fftpack import fft
#print("import success")

### method to compute absolute value of vector
def absolute_value_of_vector(vector):
    print("inside f(x)")
    for i in vector:
        for j in i:
            if j<0:
                ind = i.index(j)
                j=0-j
                del i[ind]
                i.insert(ind,j)
    return vector
    
### method to compute FFT
def ff(x,N):
    print("inside f(x)")
    result=[]
    
    i=0

    while i!=N:   
        result.append(list(x.readframes(i)))
        i+=100        
    return result

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
    
    X=absolute_value_of_vector(ff(wav,N))
    
    if k1<N and k2<N:
        f=sum(X[1:k1])/sum(X[k1:k2])
        print(f)
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
    
    