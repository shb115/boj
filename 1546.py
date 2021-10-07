n = int(input())
a = list(map(int,input().split()))
m = max(a)
sum1 = 0
for i in range(len(a)):
    a[i] = a[i] / m * 100
    sum1 = sum1 + a[i]
avg = sum1 / len(a)
print(avg)
