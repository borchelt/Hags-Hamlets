#!/usr/bin/env python3
from playsound import playsound
import time

#prints with delay and sound
def prints(var, delay =.1, sound= True):
    time.sleep(delay)

    if sound:
        playsound("line.wav", False)
    print(var)

#returnns with delay and sound    
def printr(var, delay =.1):
    time.sleep(delay)
    playsound("line.wav", False)
    return var
