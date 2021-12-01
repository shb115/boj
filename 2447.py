def Del(s,n):
    for i in range(n//3,2*n//3):
        for j in range(n//3,2*n//3):
            s[i][j] = ' '
    return s

n = int(input())
s = [['*','*','*'],['*','*','*'],['*','*','*']]
s = Del(s,3)
while len(s)<n:
    s = 3 * s
    for i in range(len(s)):
        s[i] = 3 * s[i]
    s = Del(s,len(s))


for i in range(len(s)):
    a = ''    
    for j in range(len(s[i])):
        a = a + s[i][j]
    print(a)
