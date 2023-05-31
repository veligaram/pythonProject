name=""
while len(name)==0:
    name=input("enter your name:")
print("hello"+name)
#for loop
print("\n \n \n")
for i in range(10):
    print(i+1)
for i in range(50,100,1):
    print(i)
for i in range(50,100,2):
    print(i)
for i in "Devanandh":
    print(i)
#loop control statements
print("\n \n")
while True:
    name=input("enter your name:")
    if name!="":
        break
print(name)
print("\n \n")
phone_number="9392_54_6009"
for i in phone_number:
    if i=="_":
        continue
    print(i,end="")
#nested loop
print("\n \n")
row=int(input("enter number of rows:"))
column=int(input("enter number of columns:"))
symbol=input("enter any symbol:")
for i in range(row):
    for j in range(column):
        print(symbol,end="")
    print()