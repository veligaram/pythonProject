import math
def com_per(n,r):
    com=int((math.factorial(n)/(math.factorial(r)*math.factorial(n-r))))
    per=int((math.factorial(n)/(math.factorial(n-r))))
    return per,com
print(com_per(4,2))