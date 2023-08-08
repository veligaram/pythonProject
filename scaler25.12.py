def unique_elements(tup):
    lst=[]
    for i in (tup):
         if i not in lst:
            lst.append(i)
            print(i ,':',tup.count(i))
print(unique_elements((10,8,5,2,10,15,10,8,8,2)))

