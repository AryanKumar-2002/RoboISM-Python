from tokenize import String


def dup ():
    print("Input the string : ")
    string = input ()
    length = len(string)
    for i in range(0, 2*length, 2):
        string = string[:i+1] + string[i] + string[i+1:]
    print (string)

#for testing
#dup()