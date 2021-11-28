from collections import deque
import sys

t = int(input())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    q = deque(list(map(int, sys.stdin.readline().split())))
    j = deque([i for i in range(n)])
    b = 1
    while 1:
        a = 0
        if max(q) == q[0]:
            if j[0] == m:
                a = 1
                print(b)
                break
            q.popleft()
            j.popleft()
            b = b + 1
        else:
            q.append(q[0])
            j.append(j[0])
            q.popleft()
            j.popleft()
        if a == 1:
            break
