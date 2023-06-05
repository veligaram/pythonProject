A=float(input())/100
B=float(input())
def BMI():
    bmi=round(A/(B*B),1)
    if bmi> 29.9:
        print("obese")
    elif 24.9<bmi<=29.9:
        print("over weight")
    elif 18.5<=bmi<=24.9:
        print("Normal weight")
    else:
        print("Underweight")
BMI()
