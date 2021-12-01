import sys
ps = sys.stdin.readline()
while ps != '.\n':    
    s = []    
    for i in range(len(ps) - 1):
        if ps[i] == '(':
            s.append('(')
        if ps[i] == ')':
            s.append(')')
        if ps[i] == '[':
            s.append('[')
        if ps[i] == ']':
            s.append(']')
    c = 0    
    while len(s) >= 2:
        if ')' in s:
            a = s.index(')')
        else:
            a = 102
        if ']' in s:
            b = s.index(']')
        else:
            b = 102
        if a > b:
            if b != 0 and s[b - 1] == '[':
                del s[b]
                del s[b - 1]
            else:
                print('no')
                c = 1
                break
        elif a == b:
            print('no')
            c = 1
            break
        else:
            if a != 0 and s[a - 1] == '(':
                del s[a]
                del s[a - 1]
            else:
                print('no')
                c = 1
                break
    if len(s) != 0 and c == 0:
        print('no')
    if len(s) == 0 and c == 0:
        print('yes')
    ps = sys.stdin.readline()
