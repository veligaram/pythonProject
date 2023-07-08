N=int(input())
list=[int(item) for item in input().split()]
x=int(input())
list.pop(x-1)
for i in list:
    print(i,end=' ')