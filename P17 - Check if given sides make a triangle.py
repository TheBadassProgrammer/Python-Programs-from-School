#Program_17
#Check if given sides make a triangle

a = int(input("Enter the length of first side: "))
b = int(input("Enter the length of second side: "))
c = int(input("Enter the length of third side: "))

if (a+b<c) or (a+c<b) or (b+c<a):
   print("Given sides does not make a triangle.")

else:
   print("Given sides make a triangle.")
