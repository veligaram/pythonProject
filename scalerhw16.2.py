A=list(map(int,input().split()))
B=int(input())
C=[-1]*2
for i in A:
    if i<=B:
        C[1]=i
    if i>=B:
        C[0]=i
        break
print(C)