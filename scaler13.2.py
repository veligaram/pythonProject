import math
def ps(A):
    if(round(math.sqrt(A))*round(math.sqrt(A))==A):
        return 1
    else:
        return 0
print(ps(25))