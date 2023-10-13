def info(name,job_role,salary):
    infor={}
    max_sal=-1
    max_sal=max(salary)
    for i in range(len(salary)):
        subdict={}
        subdict['role']=job_role[i]
        subdict['salary']=salary[i]
        infor[name[i]] = subdict
    return max_sal,infor
print(info(["Alex", "Adam" , "Michael" , "Sergei"],["Data_Analyst", "Data_Scientist", "HR"," Manager"],[50000 ,60000 ,55000 ,70000]))