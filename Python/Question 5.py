def isDup (num):
    for i in range(len(num)):
        flag = False
        for j in range(i+1, len(num)):
            if (num[i] == num[j]):
                flag = True
                break
        if flag: 
            print (num[i])
            break
    
#for testing
isDup ([32,64,324,88,32,32,98,34,87,94,15,15,26,26])

"""
list = [32,64,324,88,32,98,34,87,94,15,15,26]
length = len (list)
n = []
if list[i] not in n:
"""
