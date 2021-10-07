a = input()
b = [str(i) for i in range(10)]
a = a.split('-')
memo = [0 for i in range(len(a))]
for i in range(len(a)):
    a[i] = a[i].split('+')
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
    memo[i] = sum(a[i])
print(memo[0] - sum(memo[1:]))
