T=int(input())
i=0
count=0
while i<T:
    n=int(input())
    count=0
    if n==0:
        count=1
    while n>0:
        n//=10
        count+=1
    print(count)
    i+=1

