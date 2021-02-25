import sys

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
    else:
        union(b, c)
