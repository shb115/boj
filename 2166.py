import sys

N = int(sys.stdin.readline())
xy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

S = 0

for i in range(N - 1):
    S = S + xy[i][0] * xy[i + 1][1] - xy[i + 1][0] * xy[i][1]

S = abs(S + xy[N - 1][0] * xy[0][1] - xy[0][0] * xy[N - 1][1])

print(round(0.5 * S, 1))

