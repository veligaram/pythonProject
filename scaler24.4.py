def calc_acc(actual_labels,predicted_labels):
    count=0
    total=len(actual_labels)
    for i in range(len(actual_labels)):
            if actual_labels[i]==predicted_labels[i]:
                count+=1
            else:
                continue
    return (count/total)*100
print(calc_acc(['Dog','Dog','Cat','Cat','Cat'],['Cat','Dog','Cat','Dog','Cat']))
