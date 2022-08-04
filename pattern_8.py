n = int(input())
i = 1
count = 1

while(i <= n):
    j = 1
    while(j <= i):
        print(count, end = " ")
        j+= 1
        count+= 1
    print()
    i+= 1
