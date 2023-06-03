#to print the given star pattern
def star_pattern(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i==j or i==1 or j==n:#the condition for the pattern
                print('*',end="")
            else:
                print(" ",end='')
        print()#for new line
star_pattern(8)

