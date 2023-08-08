l = [ ]
def convert(b):
  if(b==0):
    return l
  digit=b%2
  l.append(digit)
  convert(b//2)

convert(6)
l.reverse()
for i in l:
  print(i,end="")