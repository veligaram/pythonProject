#You are given T test cases,each test case has an input string A. Count the number of upppercase letters in that string A.
T=int(input())
for i in range(T):
    A=input()
    count=0
for j in A:
    if j.isupper():
        count+=1
print(count)


