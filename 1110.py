N = int(input())
n = N
cnt = 0

while 1:
    n = (n % 10) * 10 + (((n // 10) + (n % 10)) % 10)
    cnt = cnt + 1
    if n == N:
        print(cnt)
        break
