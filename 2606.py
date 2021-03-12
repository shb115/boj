import sys

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)        

if __name__ == '__main__':
    com = int(input())
    K = int(input())
    dic = {}

    for i in range(com):
        dic[i + 1] = set()

    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].add(b)
        dic[b].add(a)

    visited = []
    dfs(1, dic)
    
    print(len(visited) - 1)
