def even_odd(lst):
    diff=0
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
    return even_sum - odd_sum
print(even_odd([56,63,87,24,32,13,15,19,44,52]))