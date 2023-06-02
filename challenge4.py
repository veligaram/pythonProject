N=int(input())
j=1
while j<=N:
    print("*",end=" ")
    for i in range(N-1):
        print("_",end=" ")
    j+=1
    print("*",end="")
    print("")