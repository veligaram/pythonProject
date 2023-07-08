def solve(A,B,C):
    temp=''
    for i in A:
        if ord(i)==B:
            A=A.replace(i,chr(C))
    return A
print(solve(A="aabbcc",B=98,C=100))