def sum(dict):
    sum_of_values=0
    for i in dict.values():
        sum_of_values+=i
    print(sum_of_values)
sum({"x":25,"y":25,"z":50})