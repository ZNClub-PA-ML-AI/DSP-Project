# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:15:24 2016

@author: Nevil Dsouza
"""
import wave
print("import success")

### read a wav file
with wave.open("test1.wav", mode='rb') as wav:
    print("read success")
    wav.close()
    print("close success")