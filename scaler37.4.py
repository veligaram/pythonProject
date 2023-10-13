class Smaller:
    def __init__(self,a):
        self.string=a
    def display(self):
        print("The type Name is smaller")
    def evaluate(self):
        ans=0
        for i in self.string:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                ans+=1
        print(ans)
class Larger:
    def __init__(self,a):
        self.string=a
    def display(self):
        print("The type Name is Larger")
    def evaluate(self):
        ans=0
        for i in self.string:
            if i not in ['a','e','i','o','u','A','E','I','O','U']:
                ans+=1
        print(ans)
def main(a):
    if len(a)<6:
        obj=Smaller(a)
        obj.display()
        obj.evaluate()
    else:
        obj=Larger(a)
        obj.display()
        obj.evaluate()
main("Devanandh Veligaram")
