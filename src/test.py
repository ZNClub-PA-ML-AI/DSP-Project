# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:16:29 2016

@author: Nevil Dsouza
"""

import wave
from scipy.fftpack import fft
import matplotlib.pyplot as plt
#print("import success")


### method to compute absolute value of vector
def absolute_value_of_vector(vector):
    #print("inside absolute_value_of_vector f(x)")
    result=[]
    for i in vector:
        result.append(int(round(abs(i))))
    return result
    
### method to compute FFT
def ff(x,N):
    #print("inside ff f(x)")
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
    #print("inside f(x)")
    #print("N=",N," fs=",fs)
    # threshold frequency
    F=2.1 
    
    # length of samples
    #k1=round(N*5100/fs)
    #k2=round(N*11125/fs)
    k1=10000
    k2=20000
    
    #print("values of k1,k2 are:",k1,k2)
    
    X=absolute_value_of_vector(ff(wav,N))
    
    #avgx = sum(X)/len(X)
    #N_list.append(avgx)
    
    if k1<N and k2<N:
        a=X[0:k1]
        b=X[k1:k2]
        #print(a[k1-1])
        f=sum(a)/sum(b)
        #print("f=",f)
        
        f_list.append(f)
#        fs_list.append(fs)
#        N_list.append(N)
#        k1_list.append(k1)
#        k2_list.append(k2)
#        
#       
#    if f<F:
#        print("IVR RESPONSE = YES")
#    else:
#        print("IVR RESPONSE = NO")        
    return 


    







### method to read test WAV files in database
def read_wav(inp):
    print("inside read_wav f(x)",inp)
    return "../Database/Testing/WAV/test"+str(inp)+".wav"

def test_fft(file_path):
        
    
    with wave.open(file_path, mode='rb') as wav:
        #print("read success",file_path)
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
        #print(min(X))
#        l=[i for i in range(100,50000,100)]
#        plt.hist(X, l, histtype='bar', rwidth=0.1)
#        plt.xlabel('x')
#        plt.ylabel('y')
#        plt.title('yes list histogram')
#        plt.legend()
#        plt.show()
#        
        wav.close()
        print("close success")
        





### ENTRY POINT OF PROGRAM
#file_path="../Database/Tutorials/WAV/test1.wav"

inp = input("Enter Number of files to test OR Enter * to test all files\n")

### global variables to store results


file_path=''
f_list=[]
fs_list=[]
N_list=[]
k1_list=[]
k2_list=[]

### start reading and fft

if inp=='*':
    for i in range(1,25):
        file_path=read_wav(i)            
        test_fft(file_path)
else:
    file_path=read_wav(inp)            
    test_fft(file_path)


#print(N_list)


### separate f_list into yes and no lists

yes_f=[]
yes_f.append(f_list[0])
yes_f.extend(f_list[2:7])
yes_f.append(f_list[10])
yes_f.extend(f_list[11:17])

#
#
no_f=[]
no_f.append(f_list[1])
no_f.extend(f_list[7:10])
no_f.extend(f_list[17:25])



#
##print(len(yes_f),len(no_f))

#s=1.0
#bins=[]
#bins.append(s)
#for i in range(20):
#    s=s+0.05
#    bins.append(s)
#    
#print(bins)

#### histogram
#

#plt.hist(yes_f, bins, histtype='bar', rwidth=0.5)
##plt.hist(no_f, bins, histtype='bar', rwidth=0.3)
##plt.hist(X, bins, histtype='bar', rwidth=0.05)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('yes list histogram')
#plt.legend()
#plt.show()


##plt.hist(yes_f, bins, histtype='bar', rwidth=0.3)
#plt.hist(no_f, bins, histtype='bar', rwidth=0.5)
##plt.hist(X, bins, histtype='bar', rwidth=0.05)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('no list histogram')
#plt.legend()
#plt.show()

#
#### save as png
##*
##fig = plt.figure()
##fig.savefig('foo.png')
#
#
#

