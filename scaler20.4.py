def date_format(date):
    list1=date.split('/')
    date1=list1[1]+"/"+list1[0]+"/"+list1[2]
    date2='/'.join(list1[::-1])
    return date1,date2
print(date_format("08/12/1998"))