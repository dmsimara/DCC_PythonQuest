import math

print("\nHYPOTENUSE CALCULATOR FOR ALF\n")

# code to read the lengths of the two shorter sides of a right-angled triangle from the user
side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))

# Calculating the hypotenuse using the Pythagorean theorem
hypotenuse = math.pow(side_a, 2) + math.pow(side_b, 2)
result = math.sqrt(hypotenuse)

# Displaying the calculated hypotenuse.
print("The hypotenuse of the right-angled triangle is: %.2f" % (result))