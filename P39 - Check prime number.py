n = int(input("Enter the number: "))
u = int((n)**0.5)
prime = False

if(n==2 or n==3 or n==5 or n==7):
    print(n,"is prime.")

else:
    for d in range(2, u):
        if(n%d!=0):
            prime = True
        else:
            prime = False
            break

    if(prime==True):
        print(n,"is prime.")
    else:
        print(n, "is not prime.")

