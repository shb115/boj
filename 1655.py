import sys
import heapq

N = int(sys.stdin.readline())
min_h = []
max_h = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if len(min_h) < len(max_h):
        heapq.heappush(min_h, -x)
        if len(min_h) != 0 and len(max_h) != 0 and -min_h[0] > max_h[0]:
            heapq.heappush(max_h, -heapq.heappop(min_h))
            heapq.heappush(min_h, -heapq.heappop(max_h))
    else:
        heapq.heappush(max_h, x)
        if len(min_h) != 0 and len(max_h) != 0 and -min_h[0] > max_h[0]:
            heapq.heappush(max_h, -heapq.heappop(min_h))
            heapq.heappush(min_h, -heapq.heappop(max_h))

    if len(min_h) >= len(max_h):
        print(-min_h[0])
    else:
        print(max_h[0])
