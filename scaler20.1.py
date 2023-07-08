def solve(A,B):
    res=''
    for i in range(len(A)):
        if ord(A[i])==B:
            return i
    return -1
print(solve(A="abc",B=99))