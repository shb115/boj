import sys

def kmp_failure_function(P, p):
    pi = [0 for _ in range(p)]
    j = 0

    for i in range(1, p):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]

        if P[i] == P[j]:
            j = j + 1
            pi[i] = j

    return pi

def kmp(T, P):
    t, p = len(T), len(P)
    pi = kmp_failure_function(P, p)
    j = 0
    cnt = 0

    for i in range(t):
        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]

        if T[i] == P[j]:
            if j == p - 1:
                cnt = 1
                j = pi[j]
            else:
                j = j + 1

    return cnt

n = int(sys.stdin.readline())

clock1, clock2 = [0 for _ in range(360000)], [0 for _ in range(360000)]

List1 = sorted(list(map(int, sys.stdin.readline().split())))

for i in List1:
    clock1[i] = 1
    
List2 = sorted(list(map(int, sys.stdin.readline().split())))

for i in List2:
    clock2[i] = 1

T = clock1 + clock1
P = clock2[List2[0]:List2[-1] + 1]

if kmp(T, P):
    print('possible')
else:
    print('impossible')
