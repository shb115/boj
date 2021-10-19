import sys

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
    
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int,sys.stdin.readline().split())
    print(A * B // gcd(A, B))
