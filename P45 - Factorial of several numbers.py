#Factorial of several numbers

n = 5
l = 8
while(n<l):
    
    x = n-1
    f = n
    while(x>0):
        f = f*x
        x = x-1
    print(f)
    n = n+1
