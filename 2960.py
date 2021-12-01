import sys

N, K = map(int, sys.stdin.readline().split())
N_list = [i for i in range(N, 1, -1)]
ans = []

while N_list:
    p = N_list.pop()
    ans.append(p)
    for i in range(len(N_list) - 1, -1, -1):
        if N_list[i] % p == 0:
            ans.append(N_list.pop(i))
            
print(ans[K - 1])
