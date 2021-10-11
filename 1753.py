import sys
from heapq import heappush, heappop

def dijkstra(start):
    dist[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in adj[n]:
            n_w = wei + w
            if n_w < dist[n_n]:
                dist[n_n] = n_w
                heappush(heap, [n_w, n_n])

inf = 20000 * 300000 + 1
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
adj = [[] for _ in range(V + 1)]
dist = [inf] * (V + 1)
heap = []
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append([v, w])
    
dijkstra(K)

for i in range(1, V + 1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])
