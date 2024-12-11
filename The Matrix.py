# Calculator Program: The Matrix

menu = '''1. Age Calculation
2. BMI Calculation'''

print("Welcome to the world of 1s and 0s")

while (True):

    print(menu)
    choice = int(input("Enter your choice from the above menu: "))

    if (choice == 1):  # Age Calculation
        day = int(input("Enter today's day: "))
        month = int(input("Enter ongoing month: "))
        year = int(input("Enter ongoing year: "))

        bday = int(input("Enter day of your DOB: "))
        bmonth = int(input("Enter month of your DOB: "))
        byear = int(input("Enter year of your DOB: "))

        if (day < bday):
            tday = (day + 30) - bday
            month = month - 1
        else:
            tday = day - bday

        if (month < bmonth):
            tmonth = (month + 12) - bmonth
            year = year - 1
        else:
            tmonth = month - bmonth

        tyear = year - byear

        print("You are", tyear, "years", tmonth, "months", tday, "days old :)")

    elif (choice == 2):  # BMI Calculation
        h = float(input("Enter height of the candidate(in m): "))
        w = float(input("Enter weight of the candidate(in kg): "))

        bmi = w / h ** 2

        if (bmi < 18.5):
            print("Candidate is underweight.")

        elif (bmi > 18.5 and bmi < 24.9):
            print("Candidate is normal.")

        elif (bmi > 25 and bmi < 29.9):
            print("Candidate is overweight.")

        else:
            print("Candidate is obese.")

    ask = input("Do you want to continue? Enter Y or N: ")

    if (ask.upper() == "Y"):
        continue
    elif (ask.upper() == "N"):
        break
    else:
        break

print("Thank you for using The Matrix!")
