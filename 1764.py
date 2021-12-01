import sys

N, M = map(int, sys.stdin.readline().split())
d = set([sys.stdin.readline().rstrip() for _ in range(N)])
b = set([sys.stdin.readline().rstrip() for _ in range(M)])

ans = sorted(list(d & b))

print(len(ans))
for i in ans:
    print(i)
