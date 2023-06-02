N=int(input())
for i in range(N-1):
    if i==0:
        print('*'*N)
    else:
        print("*",end="")
        print(" "*(N-i-2),end="")
        print("*",end="")
        print()
print("*")