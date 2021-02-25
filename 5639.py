import sys
sys.setrecursionlimit(10 ** 6)

def findpostorder(start, end):
    if start > end:
        return

    point = end + 1
    for mid in range(start + 1, end + 1):
        if preorder[start] < preorder[mid]:
            point = mid
            break

    findpostorder(start + 1, point - 1)
    findpostorder(point, end)
    print(preorder[start])

preorder = []

while 1:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

findpostorder(0, len(preorder) - 1)
