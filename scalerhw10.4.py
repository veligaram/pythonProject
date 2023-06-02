#program to print the pattern:
#1
#1 2
#1 2 3
#1 2 3 4
N=int(input())
j=1 #initialising
while j<=N:
    for i in range(1,j+1):
        print(i,end=" ")#here it prints the number i
    j+=1
    print("")