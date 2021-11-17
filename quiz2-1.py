# Author CCG 11/17/21

day = input("Enter the letter of the day (A - G): ")

day = day.lower()

if day == "a":
    print("You have class today because it is " + day.upper() + " day.")
elif day == "c":
    print("You have class today because it is " + day.upper() + " day.")
elif day == "e":
    print("You have class today because it is " + day.upper() + " day.")
elif day == "b":
    print("You do not have class today because it is " + day.upper() + " day.")
elif day == "d":
    print("You do not have class today because it is " + day.upper() + " day.")
elif day == "f":
    print("You do not have class today because it is " + day.upper() + " day.")
elif day == "g":
    print("You do not have class today because it is " + day.upper() + " day.")
else:
    print("Your input was not a day on the schedule")
