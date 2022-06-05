import string
def findSum (string):
    strngs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sum = 0
    for i in string:
        if i in strngs: sum += int (i)
    return sum
#for testing
#print (findSum("fsn354d5vg9fh2"))