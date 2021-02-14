import sys
from heapq import heappush, heappop

def dijkstra(start):
    dist = [inf for _ in range(V + 1)]
    dist[start], dist[0] = 0, 0
    heap = [[0, start]]
    while heap:
        d, n = heappop(heap)
        for n_n, dis in tree[n]:
            n_d = d + dis
            if n_d < dist[n_n]:
                dist[n_n] = n_d
                heappush(heap, [n_d, n_n])

    return dist

V = int(sys.stdin.readline())
tree = [[] for _ in range(V + 1)]
for i in range(V):
    inp = list(map(int, sys.stdin.readline().split()))
    inp.pop()
    leng = len(inp) // 2
    for __ in range(leng):
        a = inp.pop()
        b = inp.pop()
        tree[inp[0]].append([b, a])
inf = sys.maxsize

findpoint = dijkstra(1)
print(max(dijkstra(findpoint.index(max(findpoint)))))
