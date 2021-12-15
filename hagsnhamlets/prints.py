#!/usr/bin/env python3

#from playsound import playsound

import time
import music

i = 0 
border_left = ["#|.  ||     ", "#| . ||     ", "#|.  ||     ", "#| . ||     "]
border_right = ["        ||  .|#", "        || . |#", "        ||  .|#", "        || . |#"] 
#prints with delay and sound
def prints(var, delay =.1, sound= True):
    global i

    if(var == None):
        time.sleep(0)

    elif(len(var) > 112):
        var1 = var[0 : 122]
        var2 = var[123 : len(var)]
        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        if sound:
            music.playSound("line2.wav")
        print(border_left[i] + var1 + "-")

        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        if sound:
            music.playSound("line2.wav")
        print(border_left[i] + "-" +var2)

    else:

        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        if sound:
            music.playSound("line2.wav")
        print(border_left[i] + var)

#returnns with delay and sound    
def printr(var, delay =.1, sound = True):
    global i
    if(var == None):
        time.sleep(0)

    else:

        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        if sound:
            music.playSound("line2.wav")
        return(border_left[i] + var)

def printsl(var, delay =.1, sound= True):
    global i

    if(var == None):
        time.sleep(0)

    else:

        i += 1
        if i > 3: 
            i = 0 
        time.sleep(delay)
        if sound:
            music.playSound("line2.wav")
        print(border_left[i] + var)
