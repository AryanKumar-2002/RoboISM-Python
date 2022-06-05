def asc (string):
    orderedString = string
    for i in range(len(orderedString)):
        for j in range(i, len(orderedString)):
            if orderedString[i] > orderedString [j]:
                orderedString = orderedString[:i] + orderedString [j] + orderedString[i+1:j] + orderedString [i] + orderedString[j+1:]
    return orderedString

#for testing
#print ("Ordered string = " + asc(input("Enter your string : ")))