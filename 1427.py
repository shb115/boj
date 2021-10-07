a = list(map(int,input()))
b = sorted(a)
b.reverse()
c = ''
for i in range(len(b)):
    c = c + str(b[i])
print(c)
