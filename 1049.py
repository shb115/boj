import sys

N, M = map(int, sys.stdin.readline().split())
guitar6 = []
guitar1 = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    guitar6.append(a)
    guitar1.append(b)

a, b = min(guitar6), min(guitar1)

if a >= 6 * b:
    print(N * b)
else:
    ans = (N // 6) * a
    N = N % 6
    if a >= N * b:
        print(ans + (N * b))
    else:
        print(ans + a)
