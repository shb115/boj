N = int(input())
for i in range(N):
    print(' ' * (N - i - 1) + '*' * (i + 1))
for i in range(N - 1):
    print(' ' * (i + 1) + '*' * (N - i - 1))
