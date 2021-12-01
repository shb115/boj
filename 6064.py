import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        if r == 0:
            return b
        else:
            return gcd(b,r)

def inv(x, y, M, N):
    for i in range(N):
        if y % N == (x + (M * i)) % N:
            break
    return i

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    if abs(x - y) % gcd(M, N) != 0:
        print(-1)
    else:
        p = x + (M * inv(x, y, M, N))
        print(p)
