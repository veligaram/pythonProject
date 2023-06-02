N=int(input())
for i in range(1,N+1):
    if i==1 or i==N:
        for j in range(N):
            print("*",end="")
    else:
        for j in range(N):
            if j==0 or j==N-1:
                print("*",end="")
            else:
                print(" ",end="")
    print()