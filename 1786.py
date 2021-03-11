import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

n, m = len(T), len(P)
cnt, res = 0, []
table = [0 for _ in range(m)]
j = 0

for i in range(1, m):
    while j > 0 and P[i] != P[j]:
        j = table[j - 1]

    if P[i] == P[j]:
        j = j + 1
        table[i] = j

j = 0

for i in range(n):
    while j > 0 and T[i] != P[j]:
        j = table[j - 1]

    if T[i] == P[j]:
        if j == m - 1:
            cnt = cnt + 1
            res.append(i - m + 2)
            j = table[j]
        else:
            j = j + 1

print(cnt)
print(*res)
