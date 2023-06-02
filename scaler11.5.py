N=int(input())
for i in range(1,N+1):
    for j in range(i+1):
        if j%2==0:
            print(" ",end="")
        else:
            print(j,end="")
    print("")