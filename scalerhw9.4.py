A=int(input())
for j in range(1,A+1):
    sum=0
    for i in range(1,j):
        if j%i==0:
            sum+=i
    if sum==j:
        print(j)