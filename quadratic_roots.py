import math
# values of a, b, and c inputted by the user 
a = int(input("Please input an 'a' value (cannot be zero): "))
b = int(input("Please input a 'b' value: "))
c = int(input("Please input a 'c' value: "))

# finding discriminant 
discriminant = (b**2 - 4 * a * c)

# finding single root if discriminant = 0 
if discriminant == 0:
    print("There is 1 real root.")
    root1 = ((-1 * b) + math.sqrt(b**2 - 4 * a * c)) / (2 * a) 
    print("The root is: " + str(root1)) 
# finding 2 roots if discriminant > 0
elif discriminant > 0: 
    print("There are 2 real roots.")
    root1 = ((-1 * b) + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print("The first root is: " + str(root1))
    root2 = ((-1 * b) - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print("The second root is: " + str(root2))
# when discriminant < 0
else: 
    print("There are no real roots.")