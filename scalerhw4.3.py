A=int(input("Rating of person:"))
if A>=2100:
    print("grand master")
elif A>=1900:
    print("candidate master")
elif A>=1600:
    print("expert")
elif A>=1400:
    print("pupil")
else:
    print("Newbie")