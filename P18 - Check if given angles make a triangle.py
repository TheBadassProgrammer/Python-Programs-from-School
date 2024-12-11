#Program_18
#Check if given angles make a triangle.

a = int(input("Enter the value of first angle: "))
b = int(input("Enter the value of second angle: "))
c = int(input("Enter the value of third angle: "))

if (a+b+c==180):
   print("Given angles make a triangle.")

else:
   print("Given angles do not make a triangle.")
