import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
start, end = 0, n - 1
ans = [a[0], a[n - 1], abs(a[start] + a[end])]
if ans[2] == 0:
    start = end
elif a[start] + a[end] > 0:
    end = end - 1
else:
    start = start + 1

while start < end:
    if abs(a[start] + a[end]) < ans[2]:
        ans[0], ans[1] = a[start], a[end]
        ans[2] = abs(a[start] + a[end])
        
    if a[start] + a[end] > 0:
        end = end - 1
    else:
        start = start + 1

for i in range(2):
    print(ans[i], end = ' ')
