#rooots of the quadratic equation
A=int(input())
B=int(input())
C=int(input())
dis=(B*B)-(4*A*C)
if dis>0:
    print(1)
elif dis==0:
    print(0)
else:
    print(-1)