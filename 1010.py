T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0 for __ in range(M)] for ___ in range(N)]
    dp[0][0] = 1
    for i in range(1, M):
        dp[0][i] = i + 1
    for i in range(1, N):
        dp[i][i] = 1
        for j in range(i + 1, M):
            for k in range(i - 1, j):
                dp[i][j] = dp[i][j] + dp[i - 1][k]        
    print(dp[N - 1][M - 1])
