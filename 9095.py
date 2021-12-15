import sys

dp = [1, 2, 4]

for i in range(2, 11):
    dp.append(dp[i] + dp[i - 1] + dp[i - 2])

T = int(input())
for _ in range(T):
    print(dp[int(sys.stdin.readline()) - 1])
