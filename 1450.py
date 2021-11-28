import sys

def bf(w, s, i, j):
    if i >= len(w):
        s.append(j)
        return
    
    bf(w, s, i + 1, j)
    bf(w, s, i + 1, j + w[i])

def bs(w, t, start, end):
    while start < end:
        mid = (start + end) // 2
        if w[mid] <= t:
            start = mid + 1
        else:
            end = mid
    return end

N, C = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))

w1, w2 = w[:N // 2], w[N // 2:]
s1, s2 = [], []

bf(w1, s1, 0, 0), bf(w2, s2, 0, 0)
s1.sort(), s2.sort()

cnt = 0

for i in s1:
    if C - i < 0:
        continue
    cnt = cnt + bs(s2, C - i, 0, len(s2))

print(cnt)
