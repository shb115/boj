import sys
from heapq import heappop, heappush

def dijkstra(start):
    dist = [inf for _ in range(N + 1)]
    dist[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, weight in adj[n]:
            n_w = weight + w
            if n_w < dist[n_n]:
                dist[n_n] = n_w
                heappush(heap, [n_w, n_n])

    return dist

N, E = map(int, sys.stdin.readline().split())
inf = 800 * 200000 + 1
adj = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append([b, c])
    adj[b].append([a, c])
heap = []
v1, v2 = map(int, sys.stdin.readline().split())

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])

if cnt < inf:
    print(cnt)
else:
    print(-1)
