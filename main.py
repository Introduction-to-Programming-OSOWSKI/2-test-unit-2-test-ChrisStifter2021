
def waterstate(x):
    if x<= 32:
        return "solid"
    elif 32 <x<212:
        return "liquid"
    else:
        return "gas"


def isDozen(y):
    if y %  12==0:
        return True
    else: 
        return False


def togerman(z):
    if z=="yes":
        return "ja"
    else:
        return "nein"


def stopLight(a):
    if a=="red":
        return "stop"
    elif a=="yellow":
        return "slow"
    else:
        return "go"





