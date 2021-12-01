import sys

p_all = int(sys.stdin.readline())

p = [int(sys.stdin.readline()) for _ in range(9)]

print(p_all - sum(p))
