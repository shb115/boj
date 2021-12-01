n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
a = sorted(a)
memo = [1 for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if a[i][1] > a[j][1] and memo[i] < memo[j] + 1:
            memo[i] = memo[j] + 1
print(n - max(memo))
