alpha = ["a","b","c","d","e","f","g","h","i","j","k"]
l = len(alpha)

for i in range(len(alpha)):
    a = 0
    while(a<=i):
        print(alpha[a], end="")
        a = a+1

    l = l-1
    print("\n")
    print(" "*l, end="")


