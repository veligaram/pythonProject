A=int(input())
prime=True
for i in range(2,int(A/2)+1):
    if A%i==0:
        prime=False
        break
    if(prime):
        print("YES")
    else:
        print("NO")