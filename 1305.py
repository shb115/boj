import sys

def kmp_failure_function(a):
    table = [0 for _ in range(L)]
    j = 0
    
    for i in range(1, L):
        while j > 0 and a[i] != a[j]:
            j = table[j - 1]

        if a[i] == a[j]:
            j = j + 1
            table[i] = j

    return table

L = int(sys.stdin.readline())
ad = sys.stdin.readline().rstrip()

table = kmp_failure_function(ad)
print(L - table[-1])
