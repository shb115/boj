import sys
sys.setrecursionlimit(10 ** 6) #재귀

def preorder(in_start, in_end, post_start, post_end): #preorder를 출력하는 함수, 
    if in_start > in_end or post_start > post_end:    #in_start : inorder의 시작 index, in_end : inorder의 끝 index
        return                                        #post_start : postorder의 시작 index, post_end : postorder의 끝 index
                                                      #배열을 주고 받으면서 하면 메모리 초과가 나기 때문에 index를 이용
    x = postorder[post_end]                           #postorder의 마지막 index가 preorder의 마지막 index
    print(x, end = ' ')
    a = ind[x]                                        #ind : 각 번호의 index를 저장해놓은 배열, 매번 index 함수 이용시 시간 초과

    left = a - in_start                               #왼쪽 길이
    right = in_end - a                                #오른쪽 길이

    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)  #새로운 앞 배열에 맞게 preorder 찾기
    preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)        #새로운 뒷 배열에 맞게 preorder 찾기

n = int(sys.stdin.readline()) #정점 개수 입력값

inorder = list(map(int, sys.stdin.readline().split())) #inorder 입력값
postorder = list(map(int, sys.stdin.readline().split())) #postorder 입력값

ind = [0] * (n + 1) #ind : 각 번호의 index를 저장해놓은 배열, 매번 index 함수 이용시 시간 초과
for i in range(n):
    ind[inorder[i]] = i

preorder(0, n - 1, 0, n - 1) #전체부터 시작
