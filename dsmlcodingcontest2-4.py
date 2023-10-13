def pure_func(List):
    for i in range(len(List)):
        List[i]=i**2
    return List
original_List=[1,2,3,4]
Modifed_List=pure_func(original_List)
print("original List:",original_List)
print("Modified List:", Modifed_List)
