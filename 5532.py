L = [int(input()) for _ in range(5)]
if L[1] % L[3] == 0:
    K = L[1] // L[3]
else:
    K = L[1] // L[3] + 1
if L[2] % L[4] == 0:
    M = L[2] // L[4]
else:
    M = L[2] // L[4] + 1

print(L[0] - max(K, M))
