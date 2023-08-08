def bubble(lst):
    count=0
    temp=0
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j]=temp
                lst[j]=lst[j+1]
                temp=lst[j+1]
        count+=1
    return count
print(bubble([5, 3, 1, 9, 4]))
