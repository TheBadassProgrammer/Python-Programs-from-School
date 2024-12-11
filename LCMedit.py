a = 24
b = 12
divisible = False
i = 1

m = max((a,b))
n = min((a,b))

a = m
b = n

if(a%b==0):
    print(a, "is the LCM.")

else:
    while not divisible:
        a = a*i
        if(a%b==0):
            print(a, "is the LCM.")
            divisible = True
        i = i+1