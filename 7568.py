n = int(input())

info_list = [0 for i in range(n)]
rank_list = [1 for i in range(n)]
output_str = ''

for i in range(n):
    info_list[i] = list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        if info_list[i][0] < info_list[j][0] and info_list[i][1] < info_list[j][1]:
            rank_list[i] = rank_list[i] + 1

for i in range(len(rank_list)):
    output_str = output_str + ' ' + str(rank_list[i])

print(output_str.lstrip())
