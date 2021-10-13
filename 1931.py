import sys

n = int(input())
meeting = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
meeting = sorted(sorted(meeting), key = lambda t: t[1])
cnt = 0
time = 0
for t in meeting:
    if t[0] >= time:
        time = t[1]
        cnt = cnt + 1
print(cnt)
