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

V, E = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
graph.sort(key = lambda x: x[2])

parent = dict()
for i in range(1, V + 1):
    parent[i] = i

ans = 0

for i in range(E):
    a, b = graph[i][0], graph[i][1]

    if find(a) == find(b):
        continue
    else:
        union(a, b)
        ans = ans + graph[i][2]

print(ans)
