import sys
import heapq

N = int(input())
h = []

for _ in range(N):
    X = int(sys.stdin.readline())
    if X != 0:
        heapq.heappush(h, X)
    else:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
