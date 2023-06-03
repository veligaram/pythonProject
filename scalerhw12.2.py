#program toprint simple intrest
def simple_intrest(time,pa,ir):
    si=(pa*(1+(time/365)*(ir/100)))#formula
    ans=round(si,2)#rounding the simple intrest value
    return ans
print(simple_intrest(789,10000.0,1.3))