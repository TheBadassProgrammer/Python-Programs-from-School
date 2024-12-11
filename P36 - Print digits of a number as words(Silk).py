#Print digits of a number as words

n = int(input("Enter the number: "))
p = len(str(n))-1

if(n==0):
   print("zero")

while(n!=0):
   r=n%10**p
   n=n//10**p
   if(n==0):
      a="zero"
   elif(n==1):
      a="one"
   elif(n==2):
      a="two"
   elif(n==3):
      a="three"
   elif(n==4):
      a="four"
   elif(n==5):
      a="five"
   elif(n==6):
      a="six"
   elif(n==7):
      a="seven"
   elif(n==8):
      a="eight"
   elif(n==9):
      a="nine"
   print(a, end=" ")
   n=r
   p=p-1

if(n%10==0):
   print("zero "*(p+1))
