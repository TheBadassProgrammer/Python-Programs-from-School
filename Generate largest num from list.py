import random

#st = [3,30,34,5,9] #9534330
lst2 = [7,4,6,2,11,30,34] #7643430211

combinations_lst = []

n = int(input("How many times to run?"))
l = len(lst2)

for i in range(n):
    test_lst = random.sample(lst2, l)
    if test_lst not in combinations_lst:
        combinations_lst.append(test_lst)

alpha = ""
alpha_combinations = []

for i in combinations_lst:
    for num in i:
        a = str(num)
        alpha = alpha + a
    alpha_combinations.append(alpha)
    alpha = ""

num_combinations = []
for a in alpha_combinations:
    num_combinations.append(int(a))

number = max(num_combinations)
pos = num_combinations.index(number)

print(alpha_combinations[pos])