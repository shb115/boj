a = input()
answer = a[0]
for i in range(len(a)):
    if a[i] == '-':
        answer = answer + a[i + 1]
print(answer)
