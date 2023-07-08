A = list(map(int, input().split()))
lar = -1
slar = -1
for i in A:
    if i > lar:
        lar = i
for i in A:
    if i > slar and i != lar:
        slar = i
print(slar)
