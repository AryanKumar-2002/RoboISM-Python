def encrypt (credNum):
    encrypted = ""
    if (len(credNum) < 4): return "Error"
    for i in range(len(credNum)):
        if (i < len(credNum) - 4): encrypted = encrypted + "*"
        else: encrypted = encrypted + credNum[i]
    return encrypted

#for testing
#credNum = (input ("Enter your credit card number : "))
#print ("Encrypted format: " + encrypt(credNum))