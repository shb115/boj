import sys

def inv(n, m):
    a = n % m
    d = 1
    s = a
    
    while s != 1:
        d = d + 1
        s = (s + a) % m
        
    return d

E, S, M = map(int,sys.stdin.readline().split())
m = 15 * 28 * 19
n1, n2, n3 = 28 * 19, 15 * 19, 15 * 28
s1, s2, s3 = inv(n1, 15), inv(n2, 28), inv(n3, 19)

x = ((E * n1 * s1) + (S * n2 * s2) + (M * n3 * s3)) % m

if x == 0:
    print(m)
else:
    print(x)
