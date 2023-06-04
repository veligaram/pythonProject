#frequancy of 1
t=int(input())
for i in range(t):
    A=int(input())#taking inputs for t value
    ans=0
while A>0:
    ld=A%10#lastdigit
    if ld==1:
        ans=ans+1
    A=A//10
print(ans)