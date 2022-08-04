N = int(input())
i = 1

while(i <= N):
    j = 1
    k = 1
    while(j <= N-i):
        print(" ", end = "")
        j+= 1
    while(k <= i):
        print("*", end = "")
        k+= 1
    print()
    i+= 1