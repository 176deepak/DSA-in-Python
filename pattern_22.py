N = int(input())
row = 1

while(row <= N):
    col = 1
    # for space
    space = row-1
    while(space):
        print(end = " ")
        space-= 1
    #for numbers 
    while(col <= N-row+1):
        print(col+(row-1), end="")
        col+= 1
    print()
    row+= 1