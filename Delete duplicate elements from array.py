array = [1, 2, 3 , 4, 8, 7, 6, 5, 5, 4, 3, 4, 2, 0, 1]

for i in array:
    counter = array.count(i)
    if counter > 1:
        for counter in range(counter-1):
            array.remove(i)
    counter = 0

print(array)