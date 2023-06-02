N=int(input())
for i in range(N):
    for j in range(N+N):
        if j<=N-i:
            print("*",end="")
        elif j>N+i:
            print("*",end="")
        else:
            print(" ",end="")
    print("")