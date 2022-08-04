N = int(input())
i = 1
while(i <= N):
    j = 1
    while(j <= N):
        print(chr(65+j-1), end = " ")
        j+= 1
    i+= 1
    print()