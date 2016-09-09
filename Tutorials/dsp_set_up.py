# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:15:24 2016

@author: Nevil Dsouza
"""
import wave
print("import success")

### method to recognize a YES or a NO from wav sample
def recognize_yes_or_no(x,fs):
    print("inside f(x)")
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
    recognize_yes_or_no(wav.getnframes,wav.getframerate)    
    
    wav.close()
    print("close success")
    
    