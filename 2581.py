import sys

def prime_test(a):
    d = 0
    if a == 1:
        return 0
    for i in range(1, int(a ** (1 / 2)) + 1):
        if a % i == 0:
            d = d + 1
    if d == 1:
        return 1
    else:
        return 0

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

a = [i for i in range(M, N + 1)]
p = []

for i in range(len(a)):
    if prime_test(a[i]):
        p.append(a[i])

if p:
    print(sum(p))
    print(min(p))
else:
    print(-1)
