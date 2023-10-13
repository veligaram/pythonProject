import math
import sys
def calculate_min(a,b,c,d,n):
    num=0
    minF=sys.maxsize
    for i in range(1,n):
        fx=((a*(i**3))+(b*(i**2))+(c*i)+d)
        if minF>fx:
            minF=fx
            num=i
    return num
print(calculate_min(1,5,-3,1,150))