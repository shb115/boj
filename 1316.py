count = 0
for i in range(int(input())):
    str1 = input()
    while len(str1) != 0:
        str2 = (str1.replace(str1[0],' ')).lstrip()
        if ' ' in str2:
            break
        str1 = str2
    if len(str1) == 0:
        count = count + 1
print(count)
