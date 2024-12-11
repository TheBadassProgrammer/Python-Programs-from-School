lst = [9, 4, -2, -1, 5, 0, -5, -3, 2]
new_lst = []
pos = []
neg = []
k = 0

for i in lst:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

print(pos)
print(neg)

if len(pos)>len(neg):
    l = len(pos) 
    l2 = len(neg) 
else:
    l = len(neg) + 1
    l2 = len(pos) + 1

for j in range(l):
    new_lst.append(pos[j])
    if(k<l2):
        new_lst.append(neg[k])
        k = k+1

print(new_lst)