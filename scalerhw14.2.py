def first_multiple(ls,x):
    ans=-1
    for i in ls:
        if i%x==0:
            ans=i
            break
    return ans
print(first_multiple([2,1,2,4,3,5],4))