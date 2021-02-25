import sys

def dfs(node):
    visit = []
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    cnt_node = len(visit)
    cnt_line = 0
    for i in range(cnt_node):
        cnt_line = cnt_line + len(graph[visit[i]])

    return cnt_node, cnt_line // 2, visit

tc = 1
while 1:
    n, m = map(int, sys.stdin.readline().split())
    
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 0
    visited = []
    for i in range(1, n + 1):
        if i in visited:
            continue
        a, b, c = dfs(i)
        visited.extend(c)
        if a - b == 1:
            ans = ans + 1

    if ans == 0:
        print('Case %d: No trees.'% tc)
    elif ans == 1:
        print('Case %d: There is one tree.'% tc)
    else:
        print('Case', '%d: A forest of' % tc, ans, 'trees.')

    tc = tc + 1
