count=0
list=[int(item) for item in input().split()]
B=int(input())
for i in list:
    if i == B:
        count+=1
print(count)