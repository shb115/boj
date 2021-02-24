import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
x = int(sys.stdin.readline())
start, end = 0, n - 1
cnt = 0

while start < end:
    if a[start] + a[end] == x:
        cnt = cnt + 1
        start = start + 1
        end = end - 1
    elif a[start] + a[end] < x:
        start = start + 1
    else:
        end = end - 1

print(cnt)
