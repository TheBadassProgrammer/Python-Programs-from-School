#Check if given number is Buzz number

n = int(input("Enter the number: "))

if(n%7==0):
    print(n, "is buzz number.")
elif((n-7)%10==0):
    print(n, "is buzz number.")
else:
    print(n, "is not buzz number.")
