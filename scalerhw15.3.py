list=[int(item) for item in input().split()]
list.insert(0,list[-1])
list.pop()
print(list)