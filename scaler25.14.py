def ages(bdays_list):
    age=[]
    for i in bdays_list:
        year=i.split('/')
        age.append(2023-int(year[2]))
    return age
print(ages(['04/07/2012','11/12/1995',' 08/17/2000',' 09/04/2004',' 02/29/2001',' 23/10/1998', '03/11/1996',' 01/01/2016']))
