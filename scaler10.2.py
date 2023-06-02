A=int(input())
sum=0
temp=A
while A>0:
    sum=sum*10+(A%10)
    A=A//10
if sum==temp:
    print("YES")
else:
    print("NO")