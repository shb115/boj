import sys

T = int(sys.stdin.readline())

for _ in range(T):
    s = list(sys.stdin.readline().split())
    for i in s:
        print(i[::-1], end = ' ')
    print()
