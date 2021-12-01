a = input()
c = [ 0 for i in range(len(a)) ]
b = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in range(len(a)):
    for j in range(2,10):
        if a[i] in b[j - 2]:
            c[i] = j
print(sum(list(c))+len(a))
