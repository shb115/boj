a=[i for i in range(10)]
for i in range(10):
    a[i] = int(input()) % 42
b=set(a)
print(len(b))
