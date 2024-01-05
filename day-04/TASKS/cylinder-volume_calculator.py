import math

print("\nCYLINDER VOLUME CALCULATOR FOR ALF\n")
# code to read the radius and height of a cylinder from the user.
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# calculating the volume of the cylinder using the formula V = πr^2h.
volume = math.pi * math.pow(radius, 2) * height

# displaying the calculated volume with 2 decimal places.
print("The volume of the cylinder is: %.2f" % (volume))





