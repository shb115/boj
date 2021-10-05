N, K = int(input()), int(input())
st, en = 1, K

while st <= en:
    mid = (st + en) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt = cnt + min(N, mid // i)
    if cnt >= K:
        answer = mid
        en = mid - 1
    else:
        st = mid + 1

print(answer)
