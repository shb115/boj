import sys
from math import gcd

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

num.sort()
d = [0 for _ in range(N - 1)]
g = [0 for _ in range(N - 2)]
ans = []

for i in range(N - 1):
    d[i] = num[i + 1] - num[i]

for i in range(N - 2):
    g[i] = gcd(d[i], d[i + 1])

if N == 2:
    m = d[0]
else:
    m = min(g)

for i in range(2, m // 2 + 1):
    if m % i == 0:
        ans.append(str(i))
ans.append(str(m))

print(' '.join(ans))
