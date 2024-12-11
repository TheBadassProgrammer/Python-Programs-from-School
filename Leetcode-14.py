strs = ["ower","flow","light"]

i = 0
index = 0
length = len(strs[0])

while(i < len(strs)):
    if len(strs[i]) < length:
        length = len(strs[i])
        index = i
    i += 1
smallest = strs[index]

x = 0
count = 0
while(x < length):
    for j in range(len(strs)):   
        if strs[j].startswith(smallest[0:length-x]):
            count += 1
        else:
            count = 0
            break
    
    if count == len(strs):
        prefix = smallest[0:length-x]
        break
    
    x += 1
if x == length:
    prefix = ""

print(prefix)