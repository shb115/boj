import sys
sys.setrecursionlimit(10 ** 6)

def getMaxDistance(A, B):
    if A == W or B == W:
        return 0

    ret = cache[A][B]

    if ret != -1:
        return ret

    ret = sys.maxsize

    maxLocation = max(A, B) + 1

    distA = abs(pathA[maxLocation][0] - pathA[A][0]) + abs(pathA[maxLocation][1] - pathA[A][1])
    distB = abs(pathB[maxLocation][0] - pathB[B][0]) + abs(pathB[maxLocation][1] - pathB[B][1])

    ret1 = getMaxDistance(maxLocation, B) + distA
    ret2 = getMaxDistance(A, maxLocation) + distB

    ret = min(ret1, ret2)
    cache[A][B] = ret
    
    return ret

def reconstruct(A, B):
    if A == W or B == W:
        return

    maxLocation = max(A, B) + 1

    distA = abs(pathA[maxLocation][0] - pathA[A][0]) + abs(pathA[maxLocation][1] - pathA[A][1])
    distB = abs(pathB[maxLocation][0] - pathB[B][0]) + abs(pathB[maxLocation][1] - pathB[B][1])

    ret1 = getMaxDistance(maxLocation, B) + distA
    ret2 = getMaxDistance(A, maxLocation) + distB

    if ret1 > ret2:
        print(2)
        reconstruct(A, maxLocation)
    else:
        print(1)
        reconstruct(maxLocation, B)

N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
pathA, pathB = [[1, 1]], [[N, N]]
for _ in range(W):
    x, y = map(int, sys.stdin.readline().split())
    pathA.append([x, y])
    pathB.append([x, y])
    
cache = [[-1 for _ in range(W + 1)] for __ in range(W + 1)]

print(getMaxDistance(0, 0))
reconstruct(0, 0)
