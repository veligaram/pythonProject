#print a program of pattern *<N-2 spaces>*
N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if j==1 or j==N:
            print("*",end="")
        else:
            print(" ",end=" ")
    print("")