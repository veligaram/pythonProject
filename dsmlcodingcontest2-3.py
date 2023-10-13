def Something(S):
    up_count=0
    lo_count=0
    for i in S:
        if i.isupper():
            up_count+=1
        elif i.islower():
            lo_count+=1
    return up_count,lo_count
print(Something("The quick Brown Fox"))