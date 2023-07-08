def solve(A):
    ans=[0]*2
    vowels="aeiou"
    for i in range (0,len(A)):
        if A[i] in vowels:
            ans[0]+=1
        else:
            ans[1]+=1

    return ans
print(solve(A="devanandh"))
