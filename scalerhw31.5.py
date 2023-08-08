def first_index(lst,m,index=0):
    if len(lst) ==0:
        return -1
    if lst[0]==m:
        return index
    return first_index(lst[1:],m,index+1)
print(first_index([3,2,1,4,2,5],2))