def lid():
    A=list(map(int,input().split()))
    for i in A:
        if i%5==0 and i%7==0:
            print(i,end=" ")
lid()
