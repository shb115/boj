for i in range(int(input())):
    x, y = map(int,input().split())
    d = y - x
    c, i = 0, 1    
    while d > 0:
        d = d - i
        c = c + 1        
        if d <= 0:
            break
        d = d - i
        c = c + 1
        i = i + 1
    print(c)
