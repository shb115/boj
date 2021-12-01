import sys

a = [int(sys.stdin.readline()) for _ in range(9)]

m = max(a)

print(m)
print(a.index(m) + 1)
