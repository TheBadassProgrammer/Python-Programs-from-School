#BMI Calculator

h = float(input("Enter height of the candidate(in m): "))
w = float(input("Enter weight of the candidate(in kg): "))

bmi = w/h**2

if (bmi<18.5):
   print("Candidate is underweight.")

elif(bmi>18.5 and bmi<24.9):
   print("Candidate is normal.")

elif(bmi>25 and bmi<29.9):
   print("Candidate is overweight.")

else:
   print("Candidate is obese.")
