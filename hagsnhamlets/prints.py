#!/usr/bin/env python3

#from playsound import playsound

import time
#from ascii_art import *

i = 0 
border_left = ["#|.  ||     ", "#| . ||     ", "#|.  ||     ", "#| . ||     "]
border_right = ["        ||  .|#", "        || . |#", "        ||  .|#", "        || . |#"] 
#prints with delay and sound
def prints(var, delay =.1, sound= True):
    global i

    
    if(var == None):
        time.sleep(0)

    else:

        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        #if sound:
            #playsound("line.wav", False)
        print(border_left[i] + var)

#returnns with delay and sound    
def printr(var, delay =.1):
    global i
    if(var == None):
        time.sleep(0)

    else:

        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        #if sound:
            #playsound("line.wav", False)
        return(border_left[i] + var)

