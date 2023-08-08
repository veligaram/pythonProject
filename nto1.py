def dec(N):
    if N==1:
        print(1)
        return
    print(N)
    dec(N-1)
dec(5)