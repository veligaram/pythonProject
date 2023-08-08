def updated_menu(list):
    Menu = [['Sweet_Corn_Soup', 300.0], ['Cream_of_Tomato_Soup', 100.0], ['Bacon_and_Cheese', 150.0],
            ['Honey_Mustard', 230.0], ['Hot_Coffee', 50.0], ['Cold_Coffee', 50.0], ['Egg_Sandwiches', 130.0],
            ['Tacos', 400.0]]
    for i in list:
        for j in Menu:
            for k in range(1,len(j)):
                if i==j[k-1]:
                    j[k]+=j[k]*0.1
    return Menu
print(updated_menu(['Hot_Coffee','Cold_Coffee','Tacos']))
