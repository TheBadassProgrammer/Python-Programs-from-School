#Program_25
#Solution of quadratic equation
a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter constant: "))

sol_1 = (-b+(b*b-4*a*c)**0.5)/2*a
sol_2 = (-b-(b*b-4*a*c)**0.5)/2*a

print("Solution 1:", sol_1, "Solution 2", sol_2)
