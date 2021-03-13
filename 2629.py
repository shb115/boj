import sys

n_sinker = int(sys.stdin.readline())
wei_sinker = list(map(int, sys.stdin.readline().split()))
n_marble = int(sys.stdin.readline())
wei_marble = list(map(int, sys.stdin.readline().split()))

memo = []

for i in range(n_sinker):
    memo.append(wei_sinker[i])
    for j in range(len(memo) - 1):
        memo.append(memo[j] + wei_sinker[i])
        if memo[j] - wei_sinker[i] > 0:
            memo.append(memo[j] - wei_sinker[i])
        if wei_sinker[i] - memo[j] > 0:
            memo.append(wei_sinker[i] - memo[j])
    memo = set(memo)
    memo = list(memo)

ans = []

for i in wei_marble:
    if i in memo:
        ans.append('Y')
    else:
        ans.append('N')

print(' '.join(ans))
