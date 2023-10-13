def removeDuplicates(S):
    l = S.split()

    k = []

    for i in l:

        if (S.count(i) >= 1 and (i not in k)):
            k.append(i)

    print(' '.join(k))
removeDuplicates("I am fine and I am good")