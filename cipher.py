alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
avoided = [" ", ",", ".", "!", "@", "/", "'","#"]
lst = []
string = input("Enter the string to be encrypted: ")
n = int(input("Enter transformation number: "))

for l in string:
    if l not in avoided:
        i = alpha.index(l)
        i = i+n
        x = alpha[i]
        lst.append(x)
    else:
        lst.append(l)

for y in lst:
    print(y, end="")
    