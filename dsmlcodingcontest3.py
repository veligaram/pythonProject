import math
def no_teams(n,k,m):
    ans=int((math.factorial(n-m))/((math.factorial(k))*(math.factorial(n-m-k))))
    return ans
print(no_teams(20,5,3))