t = int(input())
for i in range(t):
    n = int(input())
    c1 = ['' for j in range(n)]
    for j in range(n):
        a, c1[j] = map(str,input().split())
    c2 = list(set(c1))
    c3 = [0 for j in range(len(c2))]
    for j in range(len(c2)):
        c3[j] = c1.count(c2[j]) + 1
    cnt = 1
    for j in range(len(c3)):
        cnt = cnt * c3[j]
    print(cnt - 1)
