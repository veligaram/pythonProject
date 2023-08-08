def sentinelSearch(ar,target,n):
  last = ar[n-1]
  ar[n-1] = target
  i = 0
  while ar[i]!=target:
    i+=1
  ar[n-1] = last
  if (i<n-1) or target==ar[n-1]:
    return i
  else:
    return -1
print(sentinelSearch([1,2,3,4,5],5,5))