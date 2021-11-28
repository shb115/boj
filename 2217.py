import sys

N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(N)]

rope.sort()
dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = rope[i] * (N - i)

print(max(dp))
