T=int(input())
i=0
while i<T:
    n=int(input())
    total=0
    while n>0:
        last=n%10
        n=n//10
        total+=last
    print(total)

    i+=1