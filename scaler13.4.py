import math
def persq(A):
    if (round(math.sqrt(A))*round(math.sqrt(A))==A):
        return round(math.sqrt(A))
    else:
        return -1
print(persq(49))