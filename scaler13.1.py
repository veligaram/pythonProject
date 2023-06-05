def corona(A,B,C):
    days=0
    while C>0:
        C+=B
        C-=A
        days+=1
    return days
print(corona(5,3,1))