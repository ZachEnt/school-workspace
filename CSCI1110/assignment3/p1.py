#   Zach Lovejoy
#   Professor Cobian
#   CSCI 1110
#   9 Decemeber 2022
#   Assignment 3



length = float(input("Enter box length (in): "))
width = float(input("Enter box width (in): "))
height = float(input("Enter box height (in): "))

surfaceArea = (2 * length * width) + (2 * length * height) + (2 * width * height)
volume = length * width * height

print("The box's surface area is ", surfaceArea, " square inches.")
print("The box's volume is ", volume, " cubic inches.")