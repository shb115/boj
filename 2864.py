s = list(input())
for i in range(len(s)):
    if s[i] == '6':
        s[i] = '5'
s = ''.join(s)
A, B = map(int, s.split())
minimum = A + B
s = list(s)
for i in range(len(s)):
    if s[i] == '5':
        s[i] = '6'
s = ''.join(s)
A, B = map(int, s.split())
maximum = A + B
print(minimum, maximum)
