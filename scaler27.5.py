def searching(arr,b):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==b:
            return mid
        elif arr[mid]<b:
            low=mid+1
        else:
            high=mid -1
    return low
print(searching([1, 3, 5, 6],5))
