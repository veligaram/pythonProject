def index(tup,elem):
    for i in tup:
        if i==elem:
            return tup.index(elem)
    else:
        return -1
print(index((10,20,30,40,50),elem=30))


