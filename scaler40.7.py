from functools import reduce
def func(integers,names,numbers):
    map_output=list(map(lambda x:x**2,integers))
    filter_output=list(filter(lambda x:len(x)<=7,names))
    reduce_output=reduce(lambda x,y:x*y,numbers)
    return map_output,filter_output,reduce_output
print(func([4, 6, 3, 9, 2, 8, 12,],["scaler", "interviewbit ","rishabh","student","course"],[4,6,9,23,5]))