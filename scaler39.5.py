def second_lowest(names,scores):
    lst=[]
    second_low_score=0
    for i in range (len(names)):
       lst.append([names[i],scores[i]])
    order=sorted(lst,key=lambda x:int(x[1]))
    for i in range(len(names)):
        if order[i][1]!=order[0][1]:
            second_low_score=order[i][1]
            break
    second_names=[x[0] for x in order if x[1]==second_low_score]
    return lst,second_low_score,second_names


print(second_lowest(["Roy","Bose","Kar","Dutta","Ghosh"],[1,3,2,1,1]))
