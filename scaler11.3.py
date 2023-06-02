N=int(input())
k=N-1
for i in range(N):
    for j in range(k):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    k-=1
    print()