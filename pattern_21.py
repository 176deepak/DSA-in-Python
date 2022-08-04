N = int(input())
i = 1

while(i <= N):
    j = 1
    #for space
    space = N-i
    while(space):
        print(end=" ")
        space-= 1
    # for numbers
    while(j <= i):
        print(i, end="")
        j+= 1
    print()
    i+= 1