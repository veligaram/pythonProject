def harmonic_sum(n):
    if n==1:
        return 1
    return round((1/n)+harmonic_sum(n-1),3)
print(harmonic_sum(7))