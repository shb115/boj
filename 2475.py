import sys

K = list(map(int, sys.stdin.readline().split()))

for i in range(len(K)):
    K[i] = K[i] ** 2

print(sum(K) % 10)
