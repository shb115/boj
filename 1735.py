import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

A1, A2 = map(int, sys.stdin.readline().split())
B1, B2 = map(int, sys.stdin.readline().split())

a, b = (B1 * A2) + (A1 * B2), A2 * B2
d = gcd(a, b)
print(a // d, b // d)
