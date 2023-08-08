def fun(i, j):
    if (i == 0):
        return j
    else:
        return fun(i - 1, j + 1)
print(fun(4,8))