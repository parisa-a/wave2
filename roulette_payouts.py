import random
import math

# generating random number 
# 00 cannot be generated, 37 takes the place of 00 and is converted later on
number = random.randint(0, 37) 

# printing what number should be paid and colour
if number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]: 
    print("The spin resulted in " + str(number) + "...")
    print("Pay" + " " + str(number))
    print("Pay Red")
elif number == 0:
    print("The spin resulted in " + str(number) + "...")
    print("Pay" + " " + str(number))
elif number == 37:
    print("The spin resulted in 00...")
    print("Pay 00")
else:
    print("The spin resulted in " + str(number) + "...")
    print("Pay" + " " + str(number))
    print("Pay Black")

# determining if odd or even
if number == 37 or number == 0:
    print() 
elif math.remainder(number, 2) == 0:
    print("Pay Even")
else: 
    print("Pay Odd")

# printing which range it is in
if number in range(1, 19): 
    print("Pay 1 to 18")
elif number in range(19, 37):
    print("Pay 19 to 36")