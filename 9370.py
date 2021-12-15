import sys
from heapq import heappop, heappush

def dijkstra(start):
    dist = [inf for _ in range(n + 1)]
    dist[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        we, nu = heappop(heap)
        for n_n, weight in adj[nu]:
            n_w = weight + we
            if n_w < dist[n_n]:
                dist[n_n] = n_w
                heappush(heap, [n_w, n_n])
                
    return dist

inf = 2000 * 50000 + 1
T = int(sys.stdin.readline())
for ___ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        adj[a].append([b, d])
        adj[b].append([a, d])
        if a == g and b == h:
            leng = d
        if a == h and b == g:
            leng = d
    destination = []
    for i in range(t):
        destination.append(int(sys.stdin.readline()))
    answer = []

    for i in destination:
        ans_ = dijkstra(s)
        g_ = dijkstra(g)
        h_ = dijkstra(h)
        if ans_[g] + leng + h_[i] == ans_[i] or ans_[h] + leng + g_[i] == ans_[i]:
            answer.append(i)

    answer.sort()
    for i in range(len(answer)):
        answer[i] = str(answer[i])
    print(' '.join(answer))
