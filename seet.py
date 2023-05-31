untensils={"fork","spoon","knife"}
dishes={"bowl","plate","cup"}
for x in untensils:
    print(x);
untensils.add("napkin")
print(untensils)
untensils.remove("fork")
print(untensils)
untensils.update(dishes)
print(untensils)
dinner_table=untensils.union(dishes)
print(dinner_table)
print(untensils.difference(dishes))
print(untensils.intersection(dishes))