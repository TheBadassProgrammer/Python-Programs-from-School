from tracemalloc import start


lst = [1,2,4,3,5,3,2,2,2,1,-8]


for n in lst:
    i = lst.index(n)
    start_sum = 0
    end_sum = 0
    for x in range(i):
        start_sum = start_sum + lst[x]
    for y in range(i+1, len(lst)):
        end_sum = end_sum + lst[y]
    
    if start_sum==end_sum:
        print("Equilibrium attained at", n)

