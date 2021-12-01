n1, m1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n1)]
n2, m2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n2)]
c = [[] for j in range(n1)]

for i in range(n1):
    for j in range(m2):
        t = 0
        for k in range(n2):
            t = t + a[i][k] * b[k][j]
        c[i].append(str(t))
    print(' '.join(c[i]))
