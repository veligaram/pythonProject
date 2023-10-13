def str(string,length):
    result=[]
    for i in string.split():
        if len(i)==length:
            result.append(i)
    return result
print(str("The world has changed and none of us can go back all we can do is our best and sometimes the best that we can do is to start over",5))

