def varyiing(lst):
    result=[]
    nested_list=lst
    for i in range(len(nested_list)):
        for j in range(len(nested_list)):
            sorted_list=sorted(nested_list[i],key=lambda x: x.count('a'),reverse=True)
        result.append(sorted_list)
    return result
print(varyiing(["mango banana guava"]))


