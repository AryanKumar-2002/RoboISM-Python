def freq(x, list):
    frequency = 0
    for i in list:
        if i == x: frequency += 1
    return frequency

def highestFreq (list):
    highFreq = 0
    for i in list:
        h = freq (i, list)
        if highFreq < h: highFreq = h
    return highFreq

#for testing
#print (highestFreq([23,25,646,5,89,23,78,45,98,23,23,86,86,2,25,86,97]))