class Circle:

    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        P=2*3.14*self.radius
        return P
    def area(self):
        A=3.14*(self.radius ** 2)
        return A
c1=Circle(6)
print(c1.area())
print(c1.perimeter())