first = [i for i in range(1, 10001)]
first = set(first)

def d(n):
    str_1 = str(n)
    list_1 = list(str_1)
    list_2 = list(map(int,list_1))
    total = n + sum(list_2)
    return total

second = [0 for i in range(1,10001)]

a = 1

while a <= 10000:
    second[a-1] = d(a)
    a = a + 1

second = set(second)
final = first - second
final = list(final)
final = sorted(final)

for i in range(len(final)):
    print(final[i])
