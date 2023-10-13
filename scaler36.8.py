def timeConv(a,b,c,d):
    class Spanoftime:
        def __init__(self,h,m):
            self.hours=h
            self.mins=m
        def displayTime(self):
            return ("{} hours and {} min".format(self.hours,self.mins))
        def addTime(t1,t2):
            t3=Spanoftime(0,0)
            m=t1.mins+t2.mins
            h=(t1.hours+t2.hours)+m//60
            if m>60:
                m=m%60
            t3.hours=h
            t3.mins=m
            return t3
        def returnMinutes(t1,t2):
            h=t1.hours+t2.hours
            m=(t1.mins+t2.mins)+h*60
            return m
    t1=Spanoftime(a,b)
    t2=Spanoftime(c,d)
    t3=Spanoftime.addTime(t1,t2)
    t3.displayTime()
    totalmin=str(Spanoftime.returnMinutes(t1,t2))
    return t3.displayTime(),("The total minutes in time t1 and t2 are: "+ totalmin)
print(timeConv(1,1,1,1))