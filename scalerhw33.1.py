import math
def possible_ways(n,k):
    ans=int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    return ans
print(possible_ways(10,2))