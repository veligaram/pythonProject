def solve(A):
    ans=[]
    for i in range(0,len(A)):
        temp=0
        for j in range(0,len(A[0])):
            temp+=A[i][j]
        ans.append(temp)
    return ans
print(solve(A=[[1,2,3],[4,5,6],[7,8,9]]))