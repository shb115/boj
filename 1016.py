MIN, MAX = map(int, input().split())

num = [1] * (MAX - MIN + 1)
cnt = 0

for i in range(2, int(MAX ** 0.5) + 1):
    squ = i * i
    q = MIN // squ

    for j in range(q, MAX // squ + 1):
        idx = squ * j - MIN

        if idx >= 0 and num[idx]:
            num[idx] = 0

print(num.count(1))
