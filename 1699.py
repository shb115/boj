import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N + 1)]
for i in range(N + 1):
    dp[i] = i

for i in range(2, N + 1):
    for j in range(1, int((i ** 0.5)) + 1):
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[N])
