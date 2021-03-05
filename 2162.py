import sys
from collections import Counter
sys.setrecursionlimit(10 ** 6)

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

def isgroup(a, b):
    x1, y1, x2, y2 = a
    x3, y3, x4, y4 = b

    p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

    if ccw(p1, p2, p3) * ccw(p1, p2, p4) > 0 or ccw(p3, p4, p1) * ccw(p3, p4, p2) > 0:
        return False
    elif ccw(p1, p2, p3) * ccw(p1, p2, p4) == 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) == 0:
        if p1 >= p2:
            p1, p2 = p2, p1

        if p3 >= p4:
            p3, p4 = p4, p3

        if p4 >= p1 and p2 >= p3:
            return True
        else:
            return False
    else:
        return True

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

N = int(sys.stdin.readline())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
parent = [i for i in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if isgroup(P[i], P[j]):
            if find(i) != find(j):
                union(i, j)

for i in range(N):
    parent[i] = find(i)

cnt = Counter(parent)

print(len(cnt))
print(cnt.most_common(1)[0][1])
