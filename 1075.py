N = int(input())
F = int(input())
n = (F - ((N // 100) * 100) % F) % F
if n >= 10:
    print(n)
else:
    print('0' + str(n))
