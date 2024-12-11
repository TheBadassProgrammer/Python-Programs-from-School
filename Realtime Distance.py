x=0
y=0
running = True

print(
"""Valid Commands:
UP n
DOWN n
LEFT n
RIGHT n
n is an integer."""
)

while running:
    step = input()
    if step == "END":
        print("Program Terminated.")
        break
    else:
        lst = step.split(" ")
        if lst[0]=="UP":
            y = y + int(lst[1])
        elif lst[0]=="DOWN":
            y = y - int(lst[1])
        elif lst[0]=="LEFT":
            x = x - int(lst[1])
        elif lst[0]=="RIGHT":
            x = x + int(lst[1])
        else:
            print("Enter valid input.")
    print("x =", x, "y =", y)
    print("Distance =", (x**2 + y**2)**0.5)


    
    
