A=list(map(int,input().split()))
res=[]
for i in range(len(A)):
    res.append(0)
for i in range(len(A)):
    res[A[i]]=i
print(res)