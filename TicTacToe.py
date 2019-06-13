matrix=[[0 for x in range(0,3)]
for y in range(0,3)]
counter=0
while counter<9:
    counter+=1
    x=int(input("x Co-ordinates for player 1:"))
    y=int(input("y Co-ordinates for player 1:"))
    matrix[x][y]="X"
    for i in range(0, 3):
        for j in range(0, 3):
            print('%s ' % (matrix[i][j]),end = '')
            if j==2:
                print()

    for l in range(0,3):
        for m in range(0,1):
            if(matrix[l][m]=='X' and matrix[l][m+1]=='X' and matrix[l][m+2]=='X'):
                print("Player 1 wins")
                break
            if(matrix[l][m]=='O' and matrix[l][m+1]=='O' and matrix[l][m+2]=='O'):
                print("Player 2 wins")
                break
    else:
        if(matrix[0][0]=='X' and matrix[1][1]=='X' and matrix[2][2]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][2]=='X' and matrix[1][1]=='X' and matrix[2][0]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][0]=='O' and matrix[1][1]=='O' and matrix[2][2]=='O'):
            print("Player 2 wins")
            break
        if(matrix[0][2]=='O' and matrix[1][1]=='O' and matrix[2][0]=='O'):
            print("Player 2 wins")
            break

    for l in range(0,1):
        for m in range(0,3):
            if(matrix[l][m]=='X' and matrix[l+1][m]=='X' and matrix[l+2][m]=='X'):
                print("Player 1 wins")
                break
            if(matrix[l][m]=='O' and matrix[l+1][m]=='O' and matrix[l+2][m]=='O'):
                print("Player 2 wins")
                break
    else:
        if(matrix[0][0]=='X' and matrix[1][1]=='X' and matrix[2][2]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][2]=='X' and matrix[1][1]=='X' and matrix[2][0]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][0]=='O' and matrix[1][1]=='O' and matrix[2][2]=='O'):
            print("Player 2 wins")
            break
        if(matrix[0][2]=='O' and matrix[1][1]=='O' and matrix[2][0]=='O'):
            print("Player 2 wins")
            break

    x1=int(input("x Co-ordinates for player 2:"))
    y1=int(input("y Co-ordinates for player 2:"))
    matrix[x1][y1]="O"
    for i in range(0, 3):
        for j in range(0, 3):
            print('%s ' % (matrix[i][j]),end = '')
            if j==2:
                print()
    for l in range(0,3):
        for m in range(0,1):
            if(matrix[l][m]=='X' and matrix[l][m+1]=='X' and matrix[l][m+2]=='X'):
                print("Player 1 wins")
                break
            if(matrix[l][m]=='O' and matrix[l][m+1]=='O' and matrix[l][m+2]=='O'):
                print("Player 2 wins")
                break
    else:
        if(matrix[0][0]=='X' and matrix[1][1]=='X' and matrix[2][2]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][2]=='X' and matrix[1][1]=='X' and matrix[2][0]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][0]=='O' and matrix[1][1]=='O' and matrix[2][2]=='O'):
            print("Player 2 wins")
            break
        if(matrix[0][2]=='O' and matrix[1][1]=='O' and matrix[2][0]=='O'):
            print("Player 2 wins")
            break

    for l in range(0,1):
        for m in range(0,3):
            if(matrix[l][m]=='X' and matrix[l+1][m]=='X' and matrix[l+2][m]=='X'):
                print("Player 1 wins")
                break
            if(matrix[l][m]=='O' and matrix[l+1][m]=='O' and matrix[l+2][m]=='O'):
                print("Player 2 wins")
                break
    else:
        if(matrix[0][0]=='X' and matrix[1][1]=='X' and matrix[2][2]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][2]=='X' and matrix[1][1]=='X' and matrix[2][0]=='X'):
            print("Player 1 wins")
            break
        if(matrix[0][0]=='O' and matrix[1][1]=='O' and matrix[2][2]=='O'):
            print("Player 2 wins")
            break
        if(matrix[0][2]=='O' and matrix[1][1]=='O' and matrix[2][0]=='O'):
            print("Player 2 wins")
            break

        else:
            if counter==9:
                k=1

if k==1:
    print("It's a draw")
