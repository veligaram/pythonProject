N=int(input())
list=[int(item) for item in input().split()]
X=int(input())
Y=int(input())
list.insert(X-1,Y)
for i in list:
    print(i,end=' ')