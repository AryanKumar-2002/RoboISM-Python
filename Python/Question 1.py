def arrange (num, order):
    if order == "asc":return asc(num)
    elif order == "des":return des(num)
    else: return num

def asc (num):
    orderedNum = num
    for i in range(len(orderedNum)):
        for j in range(i,len(orderedNum)):
            if orderedNum[i]>orderedNum [j]:
                x = orderedNum[j]
                orderedNum[j] = orderedNum[i]
                orderedNum [i] = x
    return orderedNum

def des (num):
    orderedNum = num
    for i in range(len(orderedNum)):
        for j in range(i,len(orderedNum)):
            if orderedNum[i]<orderedNum [j]:
                x = orderedNum[j]
                orderedNum[j] = orderedNum[i]
                orderedNum [i] = x
    return orderedNum

#for testing
"""
list = [24,2532,52,23,55,7988,203215]
newList = arrange (list, "asc")
print (newList)
"""