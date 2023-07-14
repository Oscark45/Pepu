# -*- coding: utf-8 -*-
# file_name.py
# Python 3.6

"""
Author:     Oscar Kaatranen
Created:    %(date)$
Modified:   %(date)$ 

Description

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()


phrases = np.array(["... were just adopted, bazinga!", "MrBeast Ooh",
                    "VTT puhdastila (ALD)", "Look at what you've done for the world, woah", 
                    "Black here plays g5. Why?!",
                    "Dream running music 2:28-2:39",
                    "Dream running music 3:22-3:25",
                    "Let me put you back together, then take you apart all over again",
                    "This time, there is more than an illusion to fear",
                    "It seems you couldn't make it to my show, so I brought the show to you!",
                    "Showtimes are on the hour, not a moment before and not a moment later",
                    "It's time to take your final bow!",
                    "I'm sorry, but there was never enough room on this stage for both of us!",
                    ])

#users = np.array(["Petrus Asikainen", "Anni Toijala", "Aaro Saastamoinen", "Jaakko Takala", "Ari Viitala", "Meri Aho",
#                  "Elias Pelo", "Patrick Linnanen", "Timo Norrkniivilä", "Aapo Laakkio", "Tuukka Mattlar"])

users = np.array(["Petrus Asikainen", "Juho Lähti", "Vesa-Pekka Rikala", "Maaria Tiiri",
                  "Jaakko Takala", "Elias Pelo", "Aapo Laakkio", "Patrick Linnanen", "Aleksi Järvinen",
                  "Aaro Saastamoinen", "Petteri Lehti", "Tuukka Mattlab", "Henri Brax",
                  "Julia Valkama"])

def score(string):
    num1 = 0
    num2 = 0
    i = 0
    j = 1
    for s in string:
        try:
            let = int(s)
            num1 *= 10
            num1 += let
            i += 1
        except ValueError:
            num2 += abs(ord(s.lower())-96)*j if s != " " else 0; j+=1
    return num1 + num2
usersF = np.array(list(map(lambda s: score(s)%28, users)))


for key, val in dict(zip(users, usersF)).items():
    print("{:<25} {:}".format(key, val))

print()
l_idx = []
print("-"*50)

#times = np.array([8, 17, 29, 45, 56, 70, 93])
#times2 = np.array([8, 23, 40, 58, 70, 80, 91, 108])
#sleeps = [times[0]] + [times[i+1] - times[i] for i in range(len(times)-1)] \
#        + [times2[0]] + [times2[i+1] - times2[i] for i in range(len(times2)-1)]
for i, ph in enumerate(phrases):
    
    
    #time.sleep(sleeps[i])
    time.sleep(5)
    if i == 6:
        #time.sleep(5)
        pass
    
    val = score(ph) 
    rem = val%26
    #print(np.abs(usersF - rem))
    idx = (np.abs(usersF - rem)).argmin()
    #print(f"\'{Fore.GREEN}{ph}{Style.BRIGHT}\'")
    print(f"\'{ph}\'")
    print("Score:", val)
    print("Remainder:", rem)
    print("\nCurrent list:\n")
    for i in range(len(users)):
        user = users[i]
        s = usersF[i]
        print("{:26}{:}".format(user, s))
    print()
    print("Pelistä putosi:", users[idx])
    print("-"*50)
    print("\n"*2)
    usersF = np.delete(usersF, idx)
    users = np.delete(users, idx)
    l_idx.append(idx)
    
    if len(usersF) == 1:
        break

time.sleep(2)
print("Winner:", users.item())