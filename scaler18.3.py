def solve(A):
    result=[]
    for i in range(len(A)):
        tmp=[]
        for j in range(len(A[i])):
            tmp.append(A[j][i])
        result.append(tmp)
    return result
print(solve(A=[[1,2,3],[4,5,6],[7,8,9]]))