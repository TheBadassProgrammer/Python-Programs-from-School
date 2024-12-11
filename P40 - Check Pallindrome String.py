#Check if a string is pallindrome or not.

str = input("Enter any string: ")

l = len(str)
pallindrome = False
i = 0
while(i<l//2):
    if(str[i]==str[l-(i+1)]):
        i+=1
        pallindrome = True
    else:
        pallindrome = False
        break

if(pallindrome):
    print("Pallindrome.")
else:
    print("Not a pallindrome.")
