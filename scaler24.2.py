def replace_cube(lst,N):
    result=lst
    for i in range(0,len(lst)):
        if lst[i]%N==0:
            lst[i]=lst[i]**3

    print(result)
replace_cube([1,2,3,4,5],2)
