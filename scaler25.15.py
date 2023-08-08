def flatten(lst):
    flatten_list=[]
    for i in lst:
        for j in i:
            flatten_list.append(j)
    return flatten_list
print(flatten(["Scaler is Awesome",["Python for Data Science",["Machine Learning"]]]))