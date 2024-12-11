#Program_21
#Find largest number among three numbers using logical and relational operator

a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
c = int(input("Enter first number: "))

if(a>b and a>c):
   print(a, "is largest.")

elif(b>a and b>c):
   print(b, "is largest.")

else:
   print(c, "is largest.")

