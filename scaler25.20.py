list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
list2 = list1
list3 = list1[:]

list2[0] = 'Guava'
list3[1] = 'Kiwi'

total = 0
for ls in (list1, list2, list3):
  if ls[0] == 'Guava':
    total += 1

  if ls[1] == 'Kiwi':
    total += 20

print (total, list3[0])