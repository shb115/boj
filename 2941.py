a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = [chr(i) for i in range(0x41,0x41+26)]
b = input()
count = 0
for i in range(len(a)):
    count = count + b.count(a[i])
    b = b.replace(a[i],' ')
b = b.replace(' ','')
print(count + len(b))
