lst1 = [1,2,3,4,7,9]
lst2 = [0,1,2,1,1,4]
count = 0

for i in lst1:
    for j in lst2:
        if i>=j:
            count = count + 1
    print(count, end = " ")
    count = 0
