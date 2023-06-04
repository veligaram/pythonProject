#gross salary
A=int(input())
if A>=20001:
    HRA=A*(30/100)
    DA=A*(95/100)
    grosssalary=A+HRA+DA
    print(grosssalary)
elif 10001<=A>20001:
    HRA=A*(25/100)
    DA=A*(90/100)
    grosssalary=A+HRA+DA
    print(grosssalary)
else:
    HRA = A * (20 / 100)
    DA = A * (80 / 100)
    grosssalary = A + HRA + DA
    print(grosssalary)