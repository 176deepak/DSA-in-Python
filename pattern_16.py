N = int(input())
i = 1

while(i <= N):
    j = 1
    while(j <= i):
        print(chr(68-(i-j)), end = " ")
        j+= 1
    i+= 1
    print()