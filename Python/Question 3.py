def operate (num1, num2, operator: str):
    if (operator == '+'): return num1 + num2
    elif (operator == '-'): return num1 - num2
    elif (operator == '*'): return num1*num2
    elif (operator == '/'): return num1/num2
    else: return "Invalid Input!"

#for testing
#print ("Result = " + str(operate (int(input( "Enter the first number : ")), int(input ("Enter the second number : ")), input ("Enter the desired operation : "))))