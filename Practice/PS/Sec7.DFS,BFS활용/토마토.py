import sys
from collections import deque
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def BFS(r, c):
        for i in range(4):
            if 0 <= r+dr[i] <= n-1 and 0 <= c+dc[i] <= m-1 and board[r+dr[i]][c+dc[i]] == 0:
                board[r+dr[i]][c+dc[i]] = 1

    if __name__ == "__main__":
        m, n = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        dis = [[0 for _ in range(m)] for _ in range(n)]
        Q = deque()
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if board[i][j] == 1:
                    Q.append((i, j))
                    dis[i][j] = 0

        while Q:
            r, c = Q.popleft()
            for i in range(4):
                if 0 <= r+dr[i] <= n-1 and 0 <= c+dc[i] <= m-1 and board[r+dr[i]][c+dc[i]] == 0:
                    dis[r+dr[i]][c+dc[i]] = dis[r][c] + 1
                    board[r+dr[i]][c+dc[i]] = 1
                    Q.append((r+dr[i], c+dc[i]))

        flag = 1
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    flag = 0
        result = 0
        if flag:
            for i in range(n):
                for j in range(m):
                    if dis[i][j] > result:
                        result = dis[i][j]
            print(result)
        else:
            print(-1)
