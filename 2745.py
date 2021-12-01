N, B = input().split()
B = int(B)
ans = 0
for i in range(len(N)):
    try:
        n = int(N[len(N) - i - 1])
    except:
        n = ord(N[len(N) - i - 1]) - 55
    ans = ans + ((B ** i) * n)
print(ans)
