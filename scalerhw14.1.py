def duplicate(ls,n):
    ans=False
    for i in range(len(ls)-1):
        if ls[i]==ls[i+1]:
            ans=True
    return ans
print(duplicate([1,2,3,3],3))