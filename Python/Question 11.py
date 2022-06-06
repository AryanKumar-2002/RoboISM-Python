def isPal (string):
    l = len(string)//2
    return True if string [:l] == "".join(reversed(string[-l:])) else False

#for testing
#print ("Is a Palindrome.") if isPal (input("Enter the string : ")) else print ("Is NOT a Palindrome.")