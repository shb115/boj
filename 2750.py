n = int(input())

input_list = [0 for i in range(n)]

for i in range(n):
    input_list[i] = int(input())

input_list = sorted(input_list)

for i in input_list:
    print(i)
