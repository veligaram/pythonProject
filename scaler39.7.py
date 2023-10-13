def len_str(lst):
    result=[]
    lst=sorted(lst)
    result=sorted(lst,key=lambda x: len(x))
    return result
print(len_str(['cccc','b', 'dd', 'aaa',]))
