import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

cost = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a].append([b, c])

start, end = map(int, sys.stdin.readline().split())

inf = sys.maxsize
dist = [inf for _ in range(n + 1)]
dist[start] = 0
path = [[] for _ in range(n + 1)]
path[start] = [start]
heap = [[0, start]]

while heap:
    now_cost, now = heappop(heap)
    if now_cost > dist[now]:
        continue
    for Next, next_cost in cost[now]:
        path_cost = next_cost + now_cost
        if path_cost < dist[Next]:
            dist[Next] = path_cost
            heappush(heap, [path_cost, Next])
            path[Next] = path[now] + [Next]

print(dist[end])
print(len(path[end]))
print(' '.join(map(str, path[end])))
