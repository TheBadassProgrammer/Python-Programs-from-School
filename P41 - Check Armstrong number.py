#Check Armstrong number

n = int(input("Enter any number: "))
n_temp = n
n2 = 0
p = len(str(n))
length = len(str(n))

while(length>=1):
    a = n_temp//(10**(length-1))
    r = n_temp%(10**(length-1))
    n2 = n2 + a**p
    n_temp = r
    length-=1
    
if(n==n2):
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
