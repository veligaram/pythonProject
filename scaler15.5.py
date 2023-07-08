T=int(input())
j=0
while j<T :
    A=int(input())
    list=[int(item) for item in input().split()]
    B=int(input())
    if B in list:
        print(1)
    else:
        print(0)
j+=1