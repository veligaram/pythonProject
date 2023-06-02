N=int(input())
for j in range(N):
    A=int(input())
    B=int(input())
    G=1
    for i in range(1,min(A,B)+1):
        if A%i==0 and B%i==0:
            G=i
    L=(A*B)//G
    print(L)