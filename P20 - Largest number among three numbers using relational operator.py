#Program_20
#Find largest number among three numbers using relational operator

a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
c = int(input("Enter first number: "))

if(a>b):
   if(a>c):
      print(a, "is largest.")
   else:
      print(c, "is largest.")

elif(b>a):
   if(b>c):
      print(b, "is largest.")
   else:
      print(c, "is largest.")
