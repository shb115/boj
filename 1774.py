import sys

def find_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

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

N, M = map(int, sys.stdin.readline().split())
universegod = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

distance = []
parent = {}
ans = 0

for i in range(N):
    x1, y1 = universegod[i][0], universegod[i][1]

    for j in range(i + 1, N):
        x2, y2 = universegod[j][0], universegod[j][1]

        distance.append([i + 1, j + 1, find_distance(x1, y1, x2, y2)])

distance.sort(key = lambda x: x[2])

for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    union(a, b)

for a, b, c in distance:
    if find(a) != find(b):
        union(a, b)
        ans = ans + c

print('%0.2f' % ans)
