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

parent = [i for i in range(n)]

ans = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if find(a) == find(b):
        ans = i + 1
        break
    else:
        union(a, b)

print(ans)
