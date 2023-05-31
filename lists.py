food=["pizza","hamburger","hotdog","spaghetti"]
print(food)
food[0]="sushi"
print(food)
for  i in food:
    print(i)
food.append("ice cream")
print(food)
food.remove("hotdog")
print(food)
food.pop()
print(food)
food.insert(0,"cake")
print(food)
food.sort()
print(food)
#2Dlists
print("\n \n")
drinks=["coffe","tea","soda"]
dinner=["pizza","hamburger","hotdog"]
dessert=["cake","ice cream"]
food=[drinks,dinner,dessert]
print(food)
print(food[0])
print(food[1])
print(food[2])
print(food[0][1])
print(food[1][2])
print(food[2][0])