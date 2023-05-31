n=int(input())
for i in range(1,n+1):
    summ=0
    temp=i
    while temp>0:
        dig=temp%10
        summ+=(dig*dig*dig)
        temp=temp//10
    if (summ==i):
        print(i)

