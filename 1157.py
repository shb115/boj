a = [0 for i in range(26)]
b = input()
for i in range(len(b)):
    c = 0x41
    for j in range(26):
        if ord(b[i]) == c or ord(b[i]) == c + 32:
            a[j] = a[j] + 1
            break
        c = c + 1
d = [i for i, j in enumerate(a) if j == max(a)]
if len(d) == 1:
    print(chr(d[0]+0x41))
else:
    print('?')
