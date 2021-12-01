import sys
n = int(input())
a = [sys.stdin.readline() for i in range(n)]
a = sorted(list(map(int,a)))
for i in a:
    print(i)
