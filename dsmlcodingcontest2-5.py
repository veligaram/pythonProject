class A:
    def __init__(self,x):
        self.x=x
    def count(self,x):
        self.x+=1
class B(A):
    def __init__(self,y=0):
        A.__init__(self,5)
        self.y=y
    def count(self):
        self.y+=2
def main():
    obj=B(6)
    obj.count()
    print(obj.x,obj.y)
main()