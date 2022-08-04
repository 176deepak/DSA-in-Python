N = int(input())
i = 1

while(i <= N):
    j = 1
    while(j <= N-i+1):
        print("*", end = "")
        j+= 1
    i+= 1
    print()