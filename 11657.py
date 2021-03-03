import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
BUS = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    BUS[A].append([B, C])

inf = 500 * 60000 + 1
DP = [inf for _ in range(N + 1)]
DP[1] = 0
heap = [[] for _ in range(N + 1)]
heap[0] = [[0, 1]]

for i in range(N):
    while heap[i]:
        w, n = heappop(heap[i])
        for new_n, wei in BUS[n]:
            new_w = wei + w
            if new_w < DP[new_n]:
                DP[new_n] = new_w
                heappush(heap[i + 1], [new_w, new_n])
if heap[N] == []:
    for i in range(2, N + 1):
        if DP[i] == inf:
            print(-1)
        else:
            print(DP[i])
else:
    print(-1)
