import sys
from heapq import heappush, heappop

def dijkstra(start):    
    dist[start] = 0    
    heappush(heap, [0, start])
    reconstruct[start] = [start]
    while heap:
         w, n = heappop(heap)
         for n_n, wei in road[n]:
             n_w = w + wei
             if n_w < dist[n_n]:
                 dist[n_n] = n_w
                 reconstruct[n_n] = reconstruct[n] + [n_n]
                 heappush(heap, [n_w, n_n])

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
road = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    road[a].append([b, c])
start, end = map(int, sys.stdin.readline().split())
inf = sys.maxsize
dist = [inf] * (n + 1)
heap = []
reconstruct = [[]] * (n + 1)

dijkstra(start)

print(dist[end])
print(len(reconstruct[end]))
for i in reconstruct[end]:
    print(i, end = ' ')
