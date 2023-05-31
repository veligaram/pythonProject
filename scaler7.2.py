n = int(input())

count = 1
for i in range(1, (n // 2) + 1):
    if n % i == 0:
        count += 1

print(count)
i=1
count1=0
while i<=n:
    if n%i==0:
        count1=count1+1
    i+=1
print(count1)