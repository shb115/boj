import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    n = pow(a, b, 10)
    if n == 0:
        print(10)
    else:
        print(n)
