def num_teams(n,k,m):
    result=findMod(n-m)//((findMod(n-m-k)*findMod(k)))
    return result
def findMod(x):
    if x==1:
        return 1
    return x*findMod(x-1)
print(num_teams(20,5,3))