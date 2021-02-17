import sys
from heapq import heappush, heappop

def dijkstra(start):    
    dist = [100000000 for _ in range(N + 1)]
    dist[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        d, n = heappop(heap)
        for n_n, dis in tree[n]:
            n_d = d + dis
            if n_d < dist[n_n]:
                dist[n_n] = n_d
                heappush(heap,[n_d, n_n])
    return dist

N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
for _ in range(1, N):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

one = dijkstra(1)
print(max(dijkstra(one.index(max(one[1:])))[1:]))
