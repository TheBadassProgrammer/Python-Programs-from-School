r = 4
c = 6

lst = []
test_lst = []

for i in range(r):
    for j in range(c):
        item = i*j
        test_lst.append(item)

i = 0  
while(i<len(test_lst)):
    x = test_lst[i:i+c]
    i = i+c
    lst.append(x)

print(lst)