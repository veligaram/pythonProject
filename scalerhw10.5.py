#print a program of pattern *<N-2 spaces>*
N=int(input())
j=1
while j<=N:
    print("*",end='')#here the solution must start with * so first i printed star
    for i in range(N-2):#given the range
        print(" ",end="")
    j+=1#increamented the j value
    print("*")#at last print *