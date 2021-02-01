'''
dfs는 재귀함수 또는 스택으로 구현가능
'''

import sys
for i in range(1, 2):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(v, path):
        global cnt
        if v == n:
            print(path)
            cnt += 1
        else:
            for x in g[v]:
                if visited[x]:
                    continue
                visited[x] = 1
                path.append(x)
                DFS(x, path)
                path.pop()
                visited[x] = 0
    if __name__ == "__main__":
        n, m = map(int, input().split())
        g = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v = map(int, input().split())
            g[u].append(v)
        visited = [0 for _ in range(n+1)]
        start = 4
        visited[start] = start
        cnt = 0
        DFS(start, [start, ])
        print(cnt)
