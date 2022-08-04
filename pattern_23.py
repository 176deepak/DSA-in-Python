N = int(input())
row = 1
count = 1

while(row <= N):
    col = 1
    #for space
    space = N-row
    while(space):
        print(end=" ")
        space-= 1
    #for count 
    while(col <= row):
        print(count, end="")
        col+= 1
        count+= 1
    print()
    row+= 1