import sys

P = [list(map(int, input().split())) for _ in range(3)]

result = P[0][0] * P[1][1] - P[1][0] * P[0][1] + P[1][0] * P[2][1] - P[2][0] * P[1][1] + P[2][0] * P[0][1] - P[0][0] * P[2][1]

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)
