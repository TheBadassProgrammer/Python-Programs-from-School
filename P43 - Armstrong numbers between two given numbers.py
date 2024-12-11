#Armstrong numbers between two given numbers

start = int(input("Enter the initial limit: "))
end = int(input("Enter the final limit: "))
num = start

while(num<=end):
    n_temp = num
    n2 = 0
    p = len(str(num))
    length = len(str(num))

    while(length>=1):
        a = n_temp//(10**(length-1))
        r = n_temp%(10**(length-1))
        n2 = n2 + a**p
        n_temp = r
        length-=1
    
    if(num==n2):
        print(num, "is an Armstrong number.")
        
    num+=1

