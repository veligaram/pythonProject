N=int(input())
for i in range(N):
    A=int(input())
    B=int(input())
    Minimum=min(A,B)
    for j in range(Minimum,0,-1):
     if A%j==0 and B%j==0:
      print(j)
      break
