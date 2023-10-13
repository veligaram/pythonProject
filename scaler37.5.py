def timeHandle(a,b,c,d):
    class Spanoftime:
        def __init__(self,hours,min):
            self.hours=hours
            self.min=min
        def display(self):
            print(f"{self.hours} hours and {self.min} min")
        def addTime(t1,t2):
            t3=Spanoftime(0,0)
            t3.hours=t1.hours+t2.hours
            t3.min=t2.min+t1.min
            if t3.min>59:
                t3.hours+=1
                t3.min=0
                if(t1.min==t2.min):
                    t3.min=t1.min-1
            return t3
        def returnMinutes(t1,t2):
            hours=(t1.hours)+(t2.hours)
            min=(t1.min)+(t2.min)
            vals=hours*60+min
            return vals
    t1=Spanoftime(a,b)
    t2=Spanoftime(c,d)
    t3=Spanoftime.addTime(t1,t2)
    t3.display()
    totalmin=str(Spanoftime.returnMinutes(t1,t2))
    return t3.display(),("The total minutes in time t1 and t2 are: "+ totalmin)
print(timeHandle(1,10,0,50))
