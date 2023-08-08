def rev(n,temp=''):
    if n==0:
        return temp
    mod = n%10
    n=n//10
    temp +=str(mod)
    return (rev(n,temp))
print(rev(123))