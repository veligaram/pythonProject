class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
    def area(self):
        return (self.length*self.breadth)
r1=Rectangle(1,2)
print(r1.perimeter())
print(r1.area())