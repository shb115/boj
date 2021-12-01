b = int(input())
num = [0 for i in range(b)]
for a in range(b):
    k = int(input())
    n = int(input())
    list_a = [[0 for i in range(n)] for i in range(k + 1)]
    list_a[0] = [i for i in range(1, n + 1)]
    for i in range(1, k + 1):
        list_a[i][0] = 1
        for j in range(1, n):
            list_a[i][j] = list_a[i][j - 1] + list_a[i - 1][j]
    num[a] = list_a[k][n - 1]
for i in range(b):
    print(num[i])
