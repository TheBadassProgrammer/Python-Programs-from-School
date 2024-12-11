def check(lst):
    count0 = 0
    count1 = 0
    for l in lst: # for checking rows
        if l[0] == l[1] and l[0] == l[2] and l[0]!=2:
            if l[0] == 0:
                count0 = count0 + 1
            else:
                count1 = count1 + 1

    c = 0
    while c<3: # for checking columns
        if lst[0][c] == lst[1][c] and lst[0][c] == lst[2][c] and l[0]!=2:
            if lst[0][c] == 0:
                count0 = count0 + 1
            else:
                count1 = count1 + 1 
        c = c+1

    if lst[0][0] == lst[1][1] and lst[0][0] == lst[2][2] and l[0]!=2: # for checking diagonals
        if lst[0][0] == 0:
            count0 = count0 + 1
        else:
            count1 = count1 + 1

    if lst[0][2] == lst[1][1] and lst[0][2] == lst[2][0] and l[0]!=2:
        if lst[0][2] == 0:
            count0 = count0 + 1
        else:
            count1 = count1 + 1
    
    if count0!=0:
        return(0)
    elif count1!=0:
        return(1)
    else:
        return(2)

lst = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]
player1 = input("Player 1: ")
player2 = input("Player 2: ")
print("Player 1 uses 0, Player 2 uses 1")
won = False

while not won:
    print("Player1's turn")
    r = int(input("Row: "))
    c = int(input("Column: "))
    lst[r][c]=0
    print(lst)
    if check(lst)==0:
        print(player1, "won!")
        won = True
        break
    
    elif check(lst)==1:
        print(player2, "won!")
        won = True
        break
    
    print("Player2's turn")
    r = int(input("Row: "))
    c = int(input("Column: "))
    lst[r][c]=1
    print(lst)
    if check(lst)==0:
        print(player1, "won!")
        won = True
    
    elif check(lst)==1:
        print(player2, "won!")
        won = True