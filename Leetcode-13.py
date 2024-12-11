roman = {"I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000
}

s = "III"
lst = list(s)
lst.reverse()
num = roman[lst[0]]
i = 1
while(i < len(lst)):
    if roman[lst[i]] < roman[lst[i-1]]:
        num -= roman[lst[i]]
    else:
        num += roman[lst[i]]
    i+=1
print(num)