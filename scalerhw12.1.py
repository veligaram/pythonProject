#program to print numbers from 1 to n and n to 1
def print_num():
    N=int(input())
    for i in range(1,N+1):# for printing 1 to n order
        print(i,end=" ")
    print("")#new line
    for j in range(N,0,-1):#for printing rverse order
        print(j,end=" ")

print_num()