def sort(lst,k):
    temp=0
    for i in range(k):
        for j in range(0,k-i-1):
         if lst[j]>lst[j+1]:
            lst[j]=temp
            lst[j]=lst[j+1]
            temp = lst[j + 1]
    return lst[0]+lst[-1]
print(sort([64,34,25,12,22,11,90],4))