T=int(input())
while T>0:
    T-=1
    number=int(input())
    revs_number=int(0)
    while(number>0):
        revs_number=(revs_number*10)+number%10
        number=number//10
    print(revs_number)