N=int(input())
list=[int(item) for item in input().split()]
for i in range(0,N):
    if list[i]<0:
        print(list[i],end=' ')
