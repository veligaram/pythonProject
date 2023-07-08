N=int(input())
list=[int(item) for item in input().split()]
for i in range(N-1,-1,-1):
    print(list[i],end=" ")