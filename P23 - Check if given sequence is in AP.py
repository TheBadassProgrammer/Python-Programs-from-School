#Program_23
#Check if given sequence is in AP

a1 = int(input("Enter first term: "))
a2 = int(input("Enter second term: "))
a3 = int(input("Enter third term: "))

d1 = a2-a1
d2 = a3-a2

if(d1==d2):
    print("Given sequence is in AP.")
else:
    print("Given sequence is not in AP.")
