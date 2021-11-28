import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sqr = []

for i in range(int(M ** (1/2)), int(N ** (1/2)) + 1):
    if i ** 2 >= M:
        sqr.append(i ** 2)

if sqr:
    print(sum(sqr))
    print(min(sqr))
else:
    print(-1)
