import sys

memo = [64, 32, 16, 8, 4, 2, 1]
X = int(sys.stdin.readline())

cnt = 0
for i in range(7):
    if X >= memo[i]:
        X = X - memo[i]
        cnt = cnt + 1

print(cnt)
