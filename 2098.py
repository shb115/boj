import sys

def find_path(last, visited):
    if visited == (1 << N) - 1:
        return W[last][0] or inf

    if dp[last][visited] is not None:
        return dp[last][visited]

    tmp = inf
    for city in range(N):
        if visited & (1 << city) == 0 and W[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
    dp[last][visited] = tmp

    return tmp

N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[None] * (1 << N) for _ in range(N)]
inf = sys.maxsize

print(find_path(0, 1))
