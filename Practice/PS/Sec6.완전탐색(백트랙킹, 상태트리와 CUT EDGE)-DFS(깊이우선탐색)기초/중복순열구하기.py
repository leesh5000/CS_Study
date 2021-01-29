'''
DFS는 이 상태트리를 어떻게 구성하냐가 Key Point이다.
'''
import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))    
    def DFS(level):
        global cnt
        if level > m:
            for i in range(1, m+1):
                print(res[i], end=' ')
            cnt += 1
            print()
        else:
            for i in range(1, n+1):
                res[level] = i
                DFS(level+1)
    if __name__ == "__main__":
        n, m = map(int, input().split())
        res = [[] for _ in range(n+1)]
        cnt = 0
        DFS(1)
        print(cnt)