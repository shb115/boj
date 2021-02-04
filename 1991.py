import sys

def preorder(a):
    if a in tree:
        print(a, end = '')
        preorder(tree[a][0])        
        preorder(tree[a][1])

def inorder(a):
    if a in tree:
        inorder(tree[a][0])
        print(a, end = '')
        inorder(tree[a][1])

def postorder(a):
    if a in tree:
        postorder(tree[a][0])
        postorder(tree[a][1])
        print(a, end = '')          

N = int(sys.stdin.readline())
tree = {}
for _ in range(N):
    a, b, c = sys.stdin.readline().rstrip().split()
    tree[a] = [b, c]

preorder('A')
print()
inorder('A')
print()
postorder('A')
