class Bill:
    def __init__(self,pre,cur):
        self.pre=pre
        self.cur=cur
    def total_bill(self):
        total=0.0
        used=self.cur - self.pre
        if used<=100:
            total=used*3.5+150
        elif used>200:
            total=100*3.5+100*5+(used-200)*8+150
        elif used>100 and used<=200:
            total=100*3.5+(used-100)*5+150
        return total
b1=Bill(200,300)
print(b1.total_bill())