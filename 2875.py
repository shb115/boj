import sys

N, M, K= map(int, sys.stdin.readline().split())

if N == 2 * M:
    print((3 * M - K) // 3)
elif N > 2 * M:
    if K > N - 2 * M:
        K = K - (N - 2 * M)
        print((3 * M - K) // 3)
    else:
        print(M)
else:
    if K > 0.5 * (2 * M - N):
        K = K - 0.5 * (2 * M - N)
        print((int(1.5 * N - K) // 3))
    else:
        print(int(0.5 * N))
