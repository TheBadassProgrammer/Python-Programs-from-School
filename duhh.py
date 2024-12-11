array1 = [-1, -3, -5, 1, 2, 3]
array1 = [5, 6, 7, 8]
array3 = [-1, -2, -3, -4]
array4 = [-7, 3, 4, 5]
array = [-1,-2, 3]
array6 = [2, -3, -4, -5, -6]
array = [-2, 9, -10, -1, -2, 11, -12]
array1 = [-1, 1, 1, 6, 6, 2, 1, 1]

n = 6

neg_count = 0
pos_count = 0
for i in array1:
    if i < 0:
        neg_count += 1
    elif i >= 0:
        pos_count +=1

if (neg_count == 0) or (len(array1) == n) or (neg_count == 1 and len(array1) > n):
    product = 1
    for i in range(n):
        product = product * max(array1)
        array1.remove(max(array1))
    print(product)

elif pos_count == 0:
    product = 1
    for i in range(n):
        product = product * min(array1)
        array1.remove(min(array1))
    print(product)

else:
    temp = []
    for neg in range(2, n+1, 2):
        pos = n - neg
        product = 1
        array_copy = list(array1)
        for i in range(neg):
            product = product * min(array_copy)
            array_copy.remove(min(array_copy))
        for j in range(pos):
            product = product * max(array_copy)
            array_copy.remove(max(array_copy))
        temp.append(product)
    product = 1
    for i in range(n):
        product = product * max(array1)
        array1.remove(max(array1))
    temp.append(product)

    print(max(temp))

