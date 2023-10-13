def mirrorChars(S,k):

  original = 'abcdefghijklmnopqrstuvwxyz'

  reverse = 'zyxwvutsrqponmlkjihgfedcba'

  dictChars = dict(zip(original,reverse))

  prefix = S[0:k+1]

  suffix = S[k+1:]

  mirror = ''

  for i in range(0,len(suffix)):

    mirror = mirror + dictChars[suffix[i]]

  print (prefix+mirror)
mirrorChars("hashing",3)