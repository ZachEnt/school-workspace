#   Zach Lovejoy
#   Professor Cobian
#   CSCI 1110
#   9 Decemeber 2022
#   Assignment 3


# Variables
nums = [] # Holds all inputs
evenSum = 0
oddSum = 0
allSum = 0

# Get 5 numbers
i = 1
while i < 6:
    nums.append(int(input("Enter number " + str(i) + "/5: ")))
    i += 1

# Add all even numbers
for i in nums:
    if i % 2 == 0:
        evenSum = evenSum + i

# Add all odd numbers
for i in nums:
    if i % 2 != 0:
        oddSum = oddSum + i

# Add all numbers      
for i in nums:
    allSum = allSum + i

# Print results
print("Sum of all even inputs: ", evenSum)
print("Sum of all odd inputs: ", oddSum)
print("Sum of all inputs: ", allSum)