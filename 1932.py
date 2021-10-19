n = int(input())
tri = [list(map(int,input().split())) for i in range(n)]
memo = [[]] * n
for i in range(n):
    if i == 0:
        memo[0] = memo[0] + [tri[0][0]]
    else:
        memo[i] = memo[i] + [tri[i][0] + memo[i - 1][0]]
        for j in range(1, len(tri[i]) - 1):
            memo[i] = memo[i] + [tri[i][j] + max(memo[i - 1][j - 1],memo[i - 1][j])]
        memo[i] = memo[i] + [tri[i][len(tri[i]) - 1] + memo[i - 1][len(tri[i]) - 2]]
print(max(memo[n-1]))
