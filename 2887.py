import sys

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(sys.stdin.readline())
location = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(N)]

location_x = sorted(location)
location_y = sorted(location, key = lambda x: x[1])
location_z = sorted(location, key = lambda x: x[2])

cost_x = sorted([[abs(location_x[i][0] - location_x[i + 1][0]), location_x[i][3], location_x[i + 1][3]] for i in range(N - 1)])
cost_y = sorted([[abs(location_y[i][1] - location_y[i + 1][1]), location_y[i][3], location_y[i + 1][3]] for i in range(N - 1)])
cost_z = sorted([[abs(location_z[i][2] - location_z[i + 1][2]), location_z[i][3], location_z[i + 1][3]] for i in range(N - 1)])

cost = sorted(cost_x + cost_y + cost_z)

parent = {}
ans = 0

for i in range(N):
    parent[i] = i

for c, a, b in cost:
    if find(a) != find(b):
        union(a, b)
        ans = ans + c

print(ans)
