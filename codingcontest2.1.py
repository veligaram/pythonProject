#Take T (number of test cases) as input.
  # For each test case, take integer A as input and print the sum of digits of that number.
T=int(input())
for i in range(T):
    A=int(input())
    sum=0
while A>0:
    id=A%10
    sum+=id
    A=A//10
print(sum)