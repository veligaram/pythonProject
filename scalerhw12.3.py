#program to find the road tax for the vehicle
def road_tax(cost):
    if cost>100000:
        return ("the road tax is ",(cost*(20/100)))
    elif 75000<cost<=100000:
        return ("the road tax is ",(cost*(15/100)))
    elif 50000<cost<=75000:
        return ("the road tax is ",(cost*(10/100)))
    else:
        return ("the road tax is ",(cost*(5/100)))
print(road_tax(25000))