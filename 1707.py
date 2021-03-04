import sys
from collections import deque

K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    
    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0 for _ in range(V + 1)]
    ans = 'YES'
    queue = deque()

    for i in range(1, V + 1):
        if color[i] == 0:
            queue.append(i)
            color[i] = 1
            while queue and ans == 'YES':
                node = queue.popleft()
                for x in graph[node]:
                    if color[x] == 0:
                        color[x] = -color[node]
                        queue.append(x)
                    elif color[x] == color[node]:
                        ans = 'NO'
                        break
            if ans == 'NO':
                break
   
    print(ans)
