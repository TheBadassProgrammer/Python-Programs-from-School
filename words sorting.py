string = "without,hello,bag,world"

lst = string.split(",")

lst.sort()

for x in lst:
    print(x, end=",")