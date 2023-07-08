A=list(map(int,input().split()))
B=int(input())
C=[]
lain=0
for i in range(len(A)):
    if A[i]==B:
        C.append(i)
        for j in range(i+1,len(A)):
            if A[j]==B:
                lain=j
        if lain!=0:
            C.append(lain)
        else:
            C.append(i)
        break
print(C)