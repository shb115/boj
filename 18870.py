import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

sort_X = sorted(list(set(X)))
dict_X = {j:i for i, j in enumerate(sort_X)}

for i in X:
    print(dict_X[i], end = ' ')
