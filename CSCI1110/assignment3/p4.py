#   Zach Lovejoy
#   Professor Cobian
#   CSCI 1110
#   10 Decemeber 2022
#   Assignment 3


n = int((input("Enter integer to check for primality: ")))

if n < 2:
    isPrime = False
else:
    for num in range(n, n + 1):
        print("MADE")
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break

if isPrime:
    print(n, "is prime")
elif isPrime == False:
    print(n, "is not prime")

# Additional Notes
# took me way too long to realize <2 is automatically not prime and was awful trying to implement it prior
