def CountHi(s,count=0):
    if len(s)<2:
        return count
    if s[0]=='h' and s[1]=='i':
        count+=1
    return CountHi(s[1:],count)
print(CountHi('hishia'))