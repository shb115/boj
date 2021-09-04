from collections import deque

n, m = map(int, input().split())
a = deque(map(int, input().split()))
q = deque(i for i in range(1, n + 1))
cnt1, cnt2 = 0, 0

while len(a) > 0:
    if a[0] == q[0]:
        a.popleft()
        q.popleft()
    else:
        if q.index(a[0]) <= len(q) // 2:
            q.append(q[0])
            q.popleft()
            cnt1 = cnt1 + 1
        else:
            q.appendleft(q[-1])
            q.pop()
            cnt2 = cnt2 + 1
print(cnt1 + cnt2)
