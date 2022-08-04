N = int(input())
i = 1

while(i <= N):
    j = 1 
    while(j <= i):
        print(chr(65+i+j-2), end = " ")
        j+= 1
    i+= 1
    print()