n=int(input())
pwr=0
dec=0
while n>0:
    last=n%10
    n=n//10
    dec=dec+(last*(2**pwr))
    pwr+=1
print(dec)
