n = int(input())

a = '666'
i = 665
count = 0

while count < n:
    if a in str(i):
        count = count + 1
        destroy = i
    i = i + 1
    
print(destroy)
