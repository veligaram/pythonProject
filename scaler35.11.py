class Student:
    def __init__(self,marks1,marks2,credits1,credits2):
        self.marks1=marks1
        self.marks2=marks2
        self.credits1=credits1
        self.credits2=credits2
    def points(self,marks):
        if marks in range(90,100):
            return 10
        elif marks in range(75,90):
            return 9
        elif marks in range(60,75):
            return 8
        elif marks in range(45,60):
            return 7
        else:
            return 0
    def gradepointaverage(self):
        if self.credits1!=0 and self.credits2!=0:
            GPA= ((self.points(self.marks1)*self.credits1)+(self.points(self.marks2)*self.credits2))/(self.credits1+self.credits2)
            return round(GPA,2)
        else:
            return "Zero credits for both subjects"
