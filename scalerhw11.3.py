N=int(input())
for i in range(1,N+1):
    for j in range(i):
        print("*",end="")
    print("")
for k in range(N,1,-1):
    for j in range(0,k-1):
        print("*",end="")
    print("")