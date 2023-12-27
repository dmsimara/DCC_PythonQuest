print("\nSIMPLE CALCULATOR FOR ALF\n")

numOne = float(input("Enter the first number: "))
numTwo = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ") [0]

if operator == '+':
    result = numOne + numTwo
    print("The result of", numOne, operator, numTwo, "is", result)
elif operator == '-':
    result = numOne - numTwo
    print("The result of", numOne, operator, numTwo, "is", result)
elif operator == 'x':
    result = numOne * numTwo
    print("The result of", numOne, operator, numTwo, "is", result)
elif operator == '/':
    result = numOne / numTwo
    print("The result of", numOne, operator, numTwo, "is", result)
else:
    print("Invalid input.")
