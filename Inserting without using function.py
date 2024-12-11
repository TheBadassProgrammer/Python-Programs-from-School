lst = [0,1,2,3,4,5,6,7,8,9]
test_lst=[77]
lst = lst + test_lst
print(lst)

y=7
index=5
i = index

x=lst[i]
lst[i]=y
if(index!=len(lst)-1):
    y=lst[i+1]
    lst[i+1]=x
              
while(i<len(lst)-3):
    x=lst[i+2]
    lst[i+2]=y

    y = lst[i+3]
    lst[i+3]=x
    i = i+2
    print(lst)

if(index%2==0):
    lst[len(lst)-1]=y

print(lst)
