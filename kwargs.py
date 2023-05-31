#**kwargs=parameters that will pack all arguments into a dictionary useful so that a function can accept a varying amount of keyword arguments
def hello(**kwargs):
   print("Hello "+kwargs['first']+" "+kwargs['last'])
hello(first ='dev',miidle='anandh',last='veligaram')
#other way
def propose(**jah):
   print(" "+jah['fir']+" "+jah['mid']+" "+jah['las'])

propose(fir="I",mid="LOVE",las="YOU")