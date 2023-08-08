def common(d1,d2):
    d3={}
    for i in d1:
        if i in d2:
            d3[i]=d1[i]+d2[i]
        else:
            pass
    print(d3)
common(d1={"a":1,"b":2,"c":3},d2={"c":4,"d":5,"e":6})
