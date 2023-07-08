def solve(A,B):
    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            A[i][j]*=B
    return A
print(solve(A=[[1,2,3],[4,5,6],[7,8,9]] ,B=2))