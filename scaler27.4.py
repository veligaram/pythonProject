def count_s(arr,B):
    n=len(arr)
    left=0
    right=n-1
    count=0
    while(left<=right):
        mid=(right+left)//2
        if (arr[mid] <=B):
            count=mid+1
            left=mid+1
        else:
            right=mid-1
    return count
print(count_s([1, 3, 4, 4, 6],4))