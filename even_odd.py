import math
# reads input from the user 
number = int(input("Enter a number: "))

# math.remainder gives the difference bw the number and the nearest multiple of y (in coordinate format, which is why it's number, 2 - in x, y)
if math.remainder(number, 2) == 0:
    print("The number you have entered is even.")
else: 
    print("The number you have entered is odd.")