#programto print numerical inverted half pyramid
N=int(input())
while N>0:
    for i in range(1,N+1):
        if(i==N):#if the n andi values are equal it prints i
            print(i)
        else:
            print(i,end=" ")
    N-=1#decrement of the N value