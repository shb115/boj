import sys
t = int(input())
for i in range(t):
    ps = sys.stdin.readline()
    a, b = 0, 0
    d = 0
    for i in range(len(ps) - 1):
        if ps[i] == '(':
            a = a + 1
        else:
            b = b + 1
        if a < b:
            print('NO')
            d = 1
            break
    if a != b and d == 0:
        print('NO')
    if a == b and d == 0:
        print('YES')
