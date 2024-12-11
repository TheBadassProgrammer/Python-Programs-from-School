#Primes between two given numbers

start = int(input("Enter the initial limit: "))
end = int(input("Enter the final limit: "))
prime = True
t = 0

for n in range(start, end):
    for i in range(2, n//2):
        if(n%i!=0):
            prime = True
        else:
            prime = False
            break
    if(prime and n!=1 and n!=4):
        print(n)
        t = t+1
        
print("Total:", t)
