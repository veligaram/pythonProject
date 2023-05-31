A=int(input())
square=0
count=1
while count<A:
    square=count*count
    if(square>A):
        break
    else:
        print(square,end=" ")
        count+=1
