def series(N):
    if N==0:
        return 0
    return N+series(N-2)
print(series(10))