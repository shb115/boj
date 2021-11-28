n = int(input())

made = n
for i in range(len(str(n)),9 * len(str(n)) + 1):
    if n - i >= 0:
        if i == sum(list(map(int,str(n-i)))):
            if made >= n - i:
                made = n - i

if made == n:
    print(0)
else:
    print(made)
