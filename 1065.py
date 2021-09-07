n = int(input())

def hansu(x):
    if x >= 10:
        str_x = str(x)
        list_intx = list(map(int,str_x))
        list_sub = [0 for i in range(len(list_intx)-1)]
        for i in range(len(list_sub)):
            list_sub[i] = list_intx[i+1] - list_intx[i]
        set_sub = set(list_sub)
        if len(set_sub) == 1:
            return 1
        else:
            return 0
    else:
        return 1

total = 0

for i in range(1,n+1):
    total = total + hansu(i)

print(total)
