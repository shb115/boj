import sys

N = int(sys.stdin.readline())

layer = []

for _ in range(N):
    s = list(sys.stdin.readline().split())

    layer.append(s[1:])

layer.sort()
floor = ''

for i in range(N):
    if i == 0:
        for j in range(len(layer[i])):
            print('--' * j + layer[i][j])
    else:
        cnt = -1

        for j in range(len(layer[i])):
            if len(layer[i - 1]) <= j or layer[i - 1][j] != layer[i][j]:
                break
            else:
                cnt= j

        for j in range(cnt + 1, len(layer[i])):
            print('--' * j + layer[i][j])
