import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    List = list(map(int, sys.stdin.readline().split()))
    print(sum(List))
