def division(tup):
    odd=[]
    even=[]
    for i in range(len(tup)):
        if i%2==0:
            even.append(tup[i])
        else:
            odd.append(tup[i])
    return tuple(odd),tuple(even)
print(division((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)))
