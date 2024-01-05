print("\nFACTORIAL CALCULATOR FOR ALF\n")


number = int(input("Please, enter a non-negative integer: "))
input_number = number
factorial = 1
   
if number < 0 :
    print("Factorial is defined is defined only for non-negative integers.")
else :
    while number > 0 :
        factorial *= number
        number -= 1


print("The factorial of %d is: %d" % (input_number, factorial))