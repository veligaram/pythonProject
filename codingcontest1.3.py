#numeric stair pattern
N=int(input())
for i in range(1,N+1):
    for j in range(1,i+1):
        if j==i:
            print(j,end=" ")
        else:
            print(j,end=" ")
    print()