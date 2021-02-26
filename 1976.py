import sys
sys.setrecursionlimit(10 ** 6)

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
M = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1:
            union(i, j)

ans = 1
for i in range(M - 1):
    if find(plan[i] - 1) != find(plan[i + 1] - 1):
        ans = 0
        break

if ans:
    print('YES')
else:
    print('NO')
