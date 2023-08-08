def euclddist(a,b):
    sqdis =(a[0]-b[0])**2 + (a[1]-b[1])**2
    return (sqdis**0.5)
def compute_Dist(lis,pnt):
    new_list=[]
    for i in range(len(lis)):
        new_list.append([euclddist(pnt,lis[i]),i])
    new_list.sort()
    intdlist=new_list[:5]
    ans=[]
    for i in range(5):
        ans.append(lis[intdlist[i][1]])
    return ans
