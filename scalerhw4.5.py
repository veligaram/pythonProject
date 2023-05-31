A=int(input())
if A in range(1,12,2):
    print(31)
elif A==2:
    print(28)
elif A in range(4,12,2):
    print(30)
else:
    print('invalid date')
