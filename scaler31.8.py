def sod(n):
    if n<=0:
        return 0
    mod=int(n%10)
    n=n/10
    return sod(n)+mod
print(sod(345))