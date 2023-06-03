#program to check whether the taken value is vowel or not
def vowel_or_not():
    n=input().lower()#making the input into lower because python is case sensitive
    if n=='a'or n=='e' or n=='i' or n=='o' or n=='u':#vowels
        return 1
    else:
        return 0
print(vowel_or_not())