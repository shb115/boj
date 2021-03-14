import sys

class Node:
    def __init__(self, i):
        self.chr = i
        self.child = {}
        self.check = False

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, s):
        cur = self.root

        for i in s:
            if i not in cur.child:
                new = Node(i)
                cur.child[i] = new
                cur = new
            else:
                cur = cur.child[i]

        cur.check = True

    def search(self, s):
        cnt = 0
        cur = self.root

        for i in s:
            cur = cur.child[i]

            if len(cur.child) > 1 or cur.check:
                cnt = cnt + 1

        return cnt

while 1:
    try:
        N = int(sys.stdin.readline())
    except:
        break
    
    s = [sys.stdin.readline().rstrip() for _ in range(N)]

    nest = Trie()

    for i in s:
        nest.insert(list(i))

    ans = 0

    for i in s:
        ans = ans + nest.search(i)

    print('%.2f' % (ans / N))
