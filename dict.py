#dictionary: a changable unordered collection of unique key:value
#pairs fast because they use hashing allows us to access avalue quickly
capitals={'usa':'washington DC','india':'new delhi','china':'beijing','russia':'mascow'}
print(capitals['russia'])#prints the value of the key russia
print(capitals.get('germany')) #if the taken key is not present in the dictionary it will print none or else it will print the value of the key
print(capitals.values())#prints the values of the dictionary
print(capitals.keys())#prints the keys of the dictionary
for key,value in capitals.items():#to print the key and value to the pair we use this loop
    print(key,value)
capitals.update({'germany':'berlin'})#adds the germany key,value to the dictionary
capitals.update({'usa':'los vegas'})#updates the usa value to losvegas
print(capitals)
capitals.pop('china')#pops out the key china from the dictionary
print(capitals)
capitals.clear() #clears every value in the dictionary
print(capitals)