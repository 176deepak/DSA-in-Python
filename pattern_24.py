N = int(input())
row = 1

while(row <= N):
    col = 1
    space = N-row
    while(space):
        print(end=" ")
        space-= 1
    while(col <= row):
        print(col, end="")
        col+= 1
    col1 = 1
    while(row > col1):
        print(row-col1, end="")
        col1+= 1
    print()
    row+= 1