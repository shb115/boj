import sys

def find_route(i, j):
    if route[i][j] == 0:
        return []

    return find_route(i, route[i][j] - 1) + [route[i][j]] + find_route(route[i][j] - 1, j)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
cost = [[100000 for _ in range(n)] for __ in range(n)]
route = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                route[i][j] = k + 1

for i in range(n):
    for j in range(n):
        print(cost[i][j], end = ' ')
    print('')

for i in range(n):
    for j in range(n):
        if cost[i][j] == 0:
            print(0)
        else:
            print(len(find_route(i, j)) + 2, i + 1, end = ' ')
            for k in find_route(i, j):
                print(k, end = ' ')
            print(j + 1)
