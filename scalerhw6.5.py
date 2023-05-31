n = int(input())
lst = []
for i in range(0, n):
    lst.append(int(input()))
for j in range(0, len(lst)):
    sum = 0
    while lst[j] >= 1:
        sum += lst[j] % 10
        lst[j] = int(lst[j] / 10)
    print(sum)