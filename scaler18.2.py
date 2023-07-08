def solve(A,B):
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[i])):
            row.append(B[i][j]-A[i][j])
        result.append(row)
    return result
print(solve(A=[[1,2,3],[4,5,6],[7,8,9]],B=[[9,8,7],[6,5,4],[3,2,1]]))