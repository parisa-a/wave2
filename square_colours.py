import math
# input from user
user_position = input("Enter a position on the chess board: ")

# finding the row - no split needed, the [] finds the position
row = user_position[0]
column = int(user_position[1])

# stating if the row starts with a black or white square 
if row in ["a", "c", "e", "g"]:
    print("The row starts with a black square.")
else: 
    print("The row starts with a white square.")

# modular arithmetic, divmod divides the number in the first position by the number in the second position and puts the remainder in the second position in the output
# remainder[1] because indexes start at zero, and need remainder from the second position
remainder = divmod(column, 2)
remainder = int(remainder[1])

# if/else statement to find which ones are black and white 
if (row in ["a", "c", "e", "g"] and remainder == 0) or (row in ["b", "d", "f", "h"] and remainder == 1):
    print("Inputted position is white.")
else: 
    print("Inputted position is black.")