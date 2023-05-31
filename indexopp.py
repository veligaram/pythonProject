#index operator: gives access to a sequance's elements(str,list,tuples)
name="devanandh"
if(name[0].lower()):#checks the conditon weather the name variable ant 0 index is lower or upper if lower then moves to inside statement
    name=name.capitalize()
print(name)
first_name=name[0:3].upper()#starting from index 0 to the third value it will convert into upper case
print(first_name)
last_name=name[4::].lower()#starting from index 4 till the end it will convert into lower case
print(last_name)
last_character=name[-1] #prints last character of name
print(last_character)
