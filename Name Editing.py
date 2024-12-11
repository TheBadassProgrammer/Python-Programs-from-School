name = "Ravi Kumar Yadav"
lst = name.split(" ")

print(lst)

name_backwards = lst[-1::-1]
for word in name_backwards:
    print(word, end=" ")

for i in range(len(lst)):
    print(lst[i][0], end=" ")