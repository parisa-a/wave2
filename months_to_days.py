# reads month from user 
month = input("Enter month: ")

# dividing it up into months 
if month == "February":
    print("There are 28 or 29 days in that month.")
elif month in ["January", "March", "May", "July", "August", "October", "December"]:
    print("There are 31 days in that month.")
else:
    print("There are 30 days in that month.")