#sum of digits of a number

n = int(input("Enter the number: "))

if(n<10 and n>0):
    print(n)

elif(n<100 and n>9):
    a = n//10
    b = n-a*10
    sum = a+b
    print(sum)

elif(n<1000 and n>99):
    a = n//100
    b = (n-a*100)//10
    c = n-a*100-b*10
    sum = a+b+c
    print(sum)

elif(n<10000 and n>999):
    a = n//1000
    b = (n-a*1000)//100
    c = (n-a*1000-b*100)//10
    d = n-a*1000-b*100-c*10
    sum = a+b+c+d
    print(sum)
