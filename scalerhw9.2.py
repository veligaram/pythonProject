N=int(input())
for j in range(2,N+1):
    factor=0
    for i in range(1,(j//2)+1):
        if j%i==0:
            factor +=1
    if factor<=1:
        print(j)