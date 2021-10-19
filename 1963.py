import math, copy
from collections import deque
import sys


def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def bfs(a, b):
    ans = 0

    q = deque([[list(str(a)), 0]])
    visited = {a}

    while 1:
        val, cnt = q.popleft()
        if int("".join(map(str, val))) == b:
            return cnt
        else:
            for i in range(4):
                for j in range(10):
                    if val[i] == str(j):
                        continue
                    else:
                        tmp = copy.deepcopy(val)
                        tmp[i] = str(j)
                        tmp_val = int(''.join(map(str, tmp)))
                        if tmp_val not in visited and tmp_val >= 1000 and isprime(tmp_val):
                            visited.add(tmp_val)
                            q.append([tmp, cnt + 1])


if __name__ == '__main__':
    
    T = int(sys.stdin.readline())
    for _ in range(T):
        p1, p2 = map(int, sys.stdin.readline().split())
        print(bfs(p1, p2))
