#program to print stair case
N=int(input())
j=1
while j<=N:
    for i in range(1,j+1):
            print("*",end="")#for the range of 1 ,j+1 the * stair case will print
    j+=1
    print("")