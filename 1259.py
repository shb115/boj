import sys

while 1:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    if s == s[::-1]:
        print('yes')
    else:
        print('no')
    
