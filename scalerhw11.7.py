N = int(input())

for i in range(0, N):
    for j in range(0, N):
        if j < i:
            print(' ', end='')
        else:
            print('*', end=' ')
    print()