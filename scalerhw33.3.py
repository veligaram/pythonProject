import math
def value(npr,ncr):
    r_fact=npr//ncr
    r=-1
    for i in range(1,r_fact//2+1):
        if(math.factorial(i)==r_fact):
            r=i
            break
    return r
print(value(990,165))