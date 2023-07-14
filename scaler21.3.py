def unique_count(tup):
    lst=[]
    for v in tup:
        if v not in lst:
            lst.append(v)
            print(v,':',tup.count(v))
unique_count((10,8,5,2,10,15,10,8,5,8,8,2))