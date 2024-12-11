n = int(input("Enter the number of terms in the expression: "))
term_lst = []

for i in range(n):
    term = input("Enter term"+str(i+1)+": ")
    term_lst.append(term)

for item in term_lst:
    lst = item.partition("x")
    coeff = int(lst[0])
    var = lst[1]
    power = int(lst[2])
    print(power*coeff, var, power-1, end="")
