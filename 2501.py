N, K = map(int, input().split())
d = []
for i in range(1, N + 1):
    if N % i == 0:
        d.append(i)

if len(d) < K:
    print(0)
else:
    print(d[K - 1])
