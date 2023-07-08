def identify(A):
    n=len(A)
    for i in range(n):
        for j in range(n):
            if i==j and A[i][j]!=1:
                return 0
            elif i!=j and A[i][j]!=0:
                return 0
    return 1
print(identify(A=[[1,0],[0,1]]))