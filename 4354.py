import sys

def kmp_failure_function(a):
    m = len(a)
    table = [0 for _ in range(m)]
    j = 0

    for i in range(1, m):
        while j > 0 and a[i] != a[j]:
            j = table[j - 1]

        if a[i] == a[j]:
            j = j + 1
            table[i] = j

    return table

s = sys.stdin.readline().rstrip()

while s != '.':
    m = len(s)
    table = kmp_failure_function(s)

    if m % (m - table[m - 1]) == 0:
        print(m // (m - table[m - 1]))
    else:
        print(1)
    
    s = sys.stdin.readline().rstrip()
