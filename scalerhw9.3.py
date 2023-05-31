N=int(input())
while N>0:
    A=int(input())
    sum=0
    for i in range(1,A):
        if A%i==0:
            sum+=i
    if sum==A:
        print("YES")
    else:
        print("NO")
    N-=1
