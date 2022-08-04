from tracemalloc import start


N = int(input())
i = 1

while(i <= N):
    j = 1
    start = i-1
    while(start):
        print(end = " ")
        start-= 1
    
    #for stars
    while(j <= N-i+1):
        print("*", end = "")
        j+= 1
    
    i+= 1
    print()