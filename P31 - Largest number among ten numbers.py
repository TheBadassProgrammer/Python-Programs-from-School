#Largest number among ten numbers

a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))
a3 = int(input("Enter third number: "))
a4 = int(input("Enter fourth number: "))
a5 = int(input("Enter fifth number: "))
a6 = int(input("Enter sixth number: "))
a7 = int(input("Enter seventh number: "))
a8 = int(input("Enter eighth number: "))
a9 = int(input("Enter ninth number: "))
a10 = int(input("Enter tenth number: "))

switch = True
a = a1
while(switch):
    if(a>=a1 and a>=a2 and a>=a3 and a>=a4 and a>=a5 and a>=a6 and a>=a7 and a>=a8 and a>=a9 and a>=a10):
        print(a, "is largest.")
        switch = False
    else:
        if(a==a1):
            a=a2
        elif(a==a2):
            a=a3
        elif(a==a3):
            a=a4
        elif(a==a4):
            a=a5
        elif(a==a5):
            a=a6
        elif(a==a6):
            a=a7
        elif(a==a7):
            a=a8
        elif(a==a8):
            a=a9
        elif(a==a9):
            a=a10
        
    
    
    
    

