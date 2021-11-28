import sys

N, M = map(int, sys.stdin.readline().split())
List = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
dp = [[0 for _ in range(M)] for __ in range(N)]
dp[0][0] = List[0][0]
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + List[i][0]

for i in range(1, M):
    dp[0][i] = dp[0][i - 1] + List[0][i]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + List[i][j]

for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())
    answer = dp[x - 1][y - 1]
    if i > 1 and j > 1:
        answer = answer - dp[x - 1][j - 2] - dp[i - 2][y - 1] + dp[i - 2][j - 2]
    elif j > 1:
        answer = answer - dp[x - 1][j - 2]
    elif i > 1:
        answer = answer - dp[i - 2][y - 1]
    print(answer)
