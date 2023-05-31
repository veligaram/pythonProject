A=int(input())
if A<500000:
    print("None")
elif A>=500000 and A<1000000:
    print("Gold")
elif A>=1000000 and A<10000000:
    print("platinum")
elif A>=10000000:
    print("Diamond")
