def solve(A,B):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]==B[i][j]:
                return "equal matrices"
            else:
                return "not equal matrices"
print(solve(A=[[1,2,3],[4,5,6],[7,8,9]],B=[[1,2,3],[4,5,6],[7,8,9]]))