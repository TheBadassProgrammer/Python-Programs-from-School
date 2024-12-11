array1 = [-1, -3, -5, 1, 2, 3]
array2 = [5, 6, 7, 8]
array3 = [-1, -2, -3, -4]
array4 = [-7, 3, 4, 5]
array1 = [-1,-2,3]
array6 = [2, -3, -4, -5, -6]
array = [-2, 9, -10, -1, -2, 11, -12]

array_copy = list(array1)

neg_count = 0
pos_count = 0
for i in array1:
    if i < 0:
        neg_count += 1
    elif i >= 0:
        pos_count +=1

if (neg_count == 0) or (len(array1) == 3) or (neg_count == 1 and len(array1) > 3):
    a = max(array1)
    array1.remove(a)
    b = max(array1)
    array1.remove(b)
    c = max(array1)
    print(a*b*c)

elif pos_count == 0:
    a = min(array1)
    array1.remove(a)
    b = min(array1)
    array1.remove(b)
    c = min(array1)
    print(a*b*c)

else:
    temp = []
    largest_neg1 = min(array1)
    array1.remove(largest_neg1)
    largest_neg2 = min(array1)
    array1.remove(largest_neg2)
    largest_pos = max(array1)
    num1 = largest_neg1 * largest_neg2 * largest_pos
    temp.append(num1)

    a = max(array_copy)
    array_copy.remove(a)
    b = max(array_copy)
    array_copy.remove(b)
    c = max(array_copy)
    num2 = a*b*c
    temp.append(num2)

    print(max(temp))