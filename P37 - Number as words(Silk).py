#Print a number in words

a=""
n = int(input("Enter the number: "))

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
elif(n==10):
   a="ten"
elif(n==11):
   a="eleven"
elif(n==12):
   a="twelve"
elif(n==13):
   a="thirteen"
elif(n==14):
   a="fourteen"
elif(n==15):
   a="fifteen"
elif(n==16):
   a="sixteen"
elif(n==17):
   a="seventeen"
elif(n==18):
   a="eighteen"
elif(n==19):
   a="nineteen"
elif(n==20):
   a="twenty"
elif(n==30):
   a="thirty"
elif(n==40):
   a="forty"
elif(n==50):
   a="fifty"
elif(n==60):
   a="sixty"
elif(n==70):
   a="seventy"
elif(n==80):
   a="eighty"
elif(n==90):
   a="ninety"
print(a)


if(n>20 and n<100 and n%10!=0):
   a=n//10
   b=n-a*10

   if(a==2):
      a="twenty"
   elif(a==3):
      a="thirty"
   elif(a==4):
      a="forty"
   elif(a==5):
      a="fifty"
   elif(a==6):
      a="sixty"
   elif(a==7):
      a="seventy"
   elif(a==8):
      a="eighty"
   elif(a==9):
      a="ninety"
   print(a, end=" ")

   if(b==1):
      b="one"
   elif(b==2):
      b="two"
   elif(b==3):
      b="three"
   elif(b==4):
      b="four"
   elif(b==5):
      b="five"
   elif(b==6):
      b="six"
   elif(b==7):
      b="seven"
   elif(b==8):
      b="eight"
   elif(b==9):
      b="nine"
   print(b)

if(n>99 and n<=500):
   a=n//100
   b=(n-a*100)//10
   c=n-a*100-b*10
   
   if(a==1):
      a="one"
   elif(a==2):
      a="two"
   elif(a==3):
      a="three"
   elif(a==4):
      a="four"
   elif(a==5):
      a="five"
   elif(a==6):
      a="six"
   elif(a==7):
      a="seven"
   elif(a==8):
      a="eight"
   elif(a==9):
      a="nine"
   print(a, "hundred", end=" ")

   
   if(b==0):
      t=""
   elif(b==1 and c==1):
      t="eleven"
   elif(b==1 and c==2):
      t="twelve"
   elif(b==1 and c==3):
      t="thirteen"
   elif(b==1 and c==4):
      t="fourteen"
   elif(b==1 and c==5):
      t="fifteen"
   elif(b==1 and c==6):
      t="sixteen"
   elif(b==1 and c==7):
      t="seventeen"
   elif(b==1 and c==8):
      t="eighteen"
   elif(b==1 and c==9):
      t="nineteen"
   elif(b==2):
      t="twenty"
   elif(b==3):
      t="thirty"
   elif(b==4):
      t="forty"
   elif(b==5):
      t="fifty"
   elif(b==6):
      t="sixty"
   elif(b==7):
      t="seventy"
   elif(b==8):
      t="eighty"
   elif(b==9):
      t="ninety"
   print(t, end=" ")

   if(c==1 and b!=1):
      c="one"
   elif(c==2 and b!=1):
      c="two"
   elif(c==3 and b!=1):
      c="three"
   elif(c==4 and b!=1):
      c="four"
   elif(c==5 and b!=1):
      c="five"
   elif(c==6 and b!=1):
      c="six"
   elif(c==7 and b!=1):
      c="seven"
   elif(c==8 and b!=1):
      c="eight"
   elif(c==9 and b!=1):
      c="nine"
   else:
      c=""
   print(c)

