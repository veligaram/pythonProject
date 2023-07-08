A=list(map(int,input().split()))
sorted=True
for i in range(len(A)-1):
    if A[i]>A[i+1]:
        sorted=False
if sorted== True:
    print(1)
else:
    print(0)