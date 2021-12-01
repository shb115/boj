import sys

t = int(input())

for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    x = eval(sys.stdin.readline().rstrip())

    error = 0
    r = 1
    front = 0

    for act in p:
        if act == 'R':
            r = not r
        else:
            try:
                if r:
                    front = front + 1
                else:
                    x.pop()
            except:
                error = 1
                break

    if error or front > len(x):
        print('error')
        continue

    if r:
        x = x[front:]
    else:
        x = list(reversed(x[front:]))
    
    for j in range(len(x)):
        x[j] = str(x[j])
    x = ','.join(x)
    print('[' + x + ']')
