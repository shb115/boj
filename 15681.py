import sys
sys.setrecursionlimit(10 ** 6)

def makeTree(currentNode, parent):
    for Node in connect[currentNode]:
        if Node != parent:
            child[currentNode].append(Node)
            parentNode[Node] = currentNode
            makeTree(Node, currentNode)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for Node in child[currentNode]:
        countSubtreeNodes(Node)
        size[currentNode] = size[currentNode] + size[Node]

N, R, Q = map(int, sys.stdin.readline().split())

connect = [[] for _ in range(N + 1)]
parentNode = [0 for _ in range(N + 1)]
child = [[] for _ in range(N + 1)]
size = [1 for _ in range(N + 1)]

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())

    connect[U].append(V)
    connect[V].append(U)

for i in connect[R]:
    parentNode[i] = R
    child[R].append(i)
    makeTree(i, R)

countSubtreeNodes(R)

for _ in range(Q):
    U = int(sys.stdin.readline())
    print(size[U])
