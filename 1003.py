dp = [[1,0],[0,1]] + [[0,0] for _ in range(39)]

for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
    
T = int(input())  #T는 테스트케이스
for i in range(T):
    N = int(input()) #N은 문제에서 주어진 N
    print(dp[N][0],dp[N][1])
