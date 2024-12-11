lst1 = [1,2,3]
lst2 = [1,2,3,4]

if len(lst2)>len(lst1):
    c = lst1
    lst1 = lst2
    lst2 = c

count = 0

for i in lst2:
    if i in lst1:
        count = count + 1

if count == len(lst2):
    print("Subset.")
else:
    print("Not subset.")
