#   Zach Lovejoy
#   Professor Cobian
#   CSCI 1110
#   9 Decemeber 2022
#   Assignment 3



windspeed = int(input("Enter wind speed (mi/h): "))

if windspeed >= 157:
    msg = "Category 5"
elif windspeed > 130 and windspeed < 156:
    msg = "Category 4"
elif windspeed > 111 and windspeed < 129:
    msg = "Category 3"
elif windspeed > 96 and windspeed < 110:
    msg = "Category 2"
elif windspeed > 74 and windspeed < 95:
    msg = "Category 1"
elif windspeed <= 73:
    msg = "Non-hurricane winds"
else:
    msg = "Invalid Input!"

print(msg)