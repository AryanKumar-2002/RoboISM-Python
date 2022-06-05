def swap (x, y):
    x ^= y
    y ^= x
    x ^= y
    return x, y

#for testing 
#print ("Swapped vales = " + str (swap (int(input("Enter the first number: ")), int(input("Enter the second number: ")))))