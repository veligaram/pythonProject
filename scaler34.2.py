def frequency(arr):
    mp={}
    n=len(arr)
    for i in range(n):
        if(arr[i] not in mp):
            mp[arr[i]]=0
        mp[arr[i]]+=1
    for i in range(n):
        if(mp[arr[i]]!=-1):
            print(arr[i],mp[arr[i]])
        mp[arr[i]]=-1
frequency([10,20,10,3,4,10,4,5,3,6])