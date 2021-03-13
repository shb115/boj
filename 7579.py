import sys

N, M = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(10001)] for _ in range(N+1)]
result = 10000

for i in range(N):
    for j in range(1, 10001):
        if j < cost[i]: 
            dp[i][j] = dp[i - 1][j]
        else:        	
            dp[i][j] = max(memory[i] + dp[i - 1][j - cost[i]], dp[i - 1][j])
            
        if dp[i][j] >= M:
            result = min(result, j) 

print(result)
