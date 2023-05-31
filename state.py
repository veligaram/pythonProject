age=int(input("enter your age:"))
if age>60:
    print("you are a senior citizen")
elif age>=18 and age<60:
    print("you are  an adult")
elif age<0:
    print("you are not born yet")
else:
    print("you are a child")
#logical operator
print("\n\n\n")
temp=int(input("what is the outside temperature:"))
if temp>=0 and temp<=30:
    print("the temperature is good today")
    print("go outside")
elif temp<0 and temp>30:
    print("the temperature is bad today")
    print("stay inside")
if not(temp>=0 and temp<=30):
    print("the temperature is bad today")
    print("stay inside")
elif not( temp<0 and temp>30):
    print("the temperature is good today")
    print("go outside")
