#program to check whether the number is perfect or not
def perfect_num(n):
    sum=0#initialization
    for i in range(1,n):#we have taken this range because we dont take n as divisor
        if n%i==0:
            sum+=i#adding the divisors
    if sum==n:#perfect number
        return 1
    else:#not a perfect number
        return 0
print(perfect_num(10))
