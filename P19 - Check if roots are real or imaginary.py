#Program_19
#Check if roots of quadratic equation are real or imaginary.

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))

d = b**2-4*a*c

if (d<0):
   print("Roots are imaginary.")

elif(d==0):
   print("Roots are real and equal.")

else:
   print("Roots are real and distinct.")
