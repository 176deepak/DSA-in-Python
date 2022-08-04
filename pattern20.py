N = int(input())
i = 1

while(i <= N):
    j  = 1
    space = i-1
    # for space
    while(space):
        print(end=" ")
        space-= 1
    #for numbers
    while(j <= N-i+1):
        print(i, end="")
        j+= 1
    i+=1
    print()