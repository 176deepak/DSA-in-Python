N = int(input())
row = 1

while(row  <= N):
    col = 1
    star = row-1
    star1 = row-1
    # 1 loop
    while(col <= N-row+1):
        print(col, end="")
        col+= 1
    # 2nd loop(star)
    while(star):
        print("*", end="")
        star-= 1
    # 3rd loop(star)
    while(star1):
        print("*", end="")
        star1-= 1
    # 4th loop
    while(col-1):
        print(col-1,end="")
        col-= 1
    row+= 1
    print()