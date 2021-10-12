import sys

def add(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))

def dca(f):
    n = len(f)
    
    if n == 3:
        temp = []
        for i in range(3):
            for x in f[i]:
                temp.append(x)
        u, v = temp.count(-1), temp.count(0)
        w = 9 - u - v    
    else:
        base = (0, 0, 0)
        for i in range(0, n, n // 3):
            for j in range(0, n, n // 3):
                temp = [x[j : j + n // 3] for x in f[i : i + n // 3]]
                base = add(base, dca(temp))
        u, v, w = base

    if not any([v, w]):
        return (1, 0, 0)
    elif not any([u, w]):
        return (0, 1, 0)
    elif not any([u, v]):
        return (0, 0, 1)
    else:
        return (u, v, w)

n = int(input())
cp = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

a = dca(cp)
print(a[0])
print(a[1])
print(a[2])
