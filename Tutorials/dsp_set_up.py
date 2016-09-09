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
    print("inside absolute_value_of_vector f(x)")
    result=[]
    for i in vector:
        result.append(int(round(abs(i))))
    return result
    
### method to compute FFT
def ff(x,N):
    print("inside ff f(x)")
    result=[]
    
    i=0

    while i<=N:   
        #result.append(list(x.readframes(i)))
        temp = list(x.readframes(i))
        for i in temp:
            result.append(i)
        i+=100    
#    
#    print("FFT is ",type(FFT))
#    FFTlist = FFT.tolist()
#    print("LIST is ",FFTlist[0],type(FFTlist[0]),abs(FFTlist[0]))
#    
    return fft(result)

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
        a=X[0:k1]
        b=X[k1:k2]
        #print(a[k1-1])
        f=sum(a)/sum(b)
        print("f=",f)
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
    
    