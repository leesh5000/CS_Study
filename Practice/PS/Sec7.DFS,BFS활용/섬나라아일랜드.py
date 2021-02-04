import sys
from collections import deque
for i in range(1, 6):

    def BFS(r, c):
        Q = deque()
        Q.append((r, c))
        while Q:
            now = Q.popleft()
            board[now[0]][now[1]] = 0
            for i in range(8):
                if 0 <= now[0]+dr[i] <= n-1 and 0 <= now[1]+dc[i] <= n-1 and board[now[0]+dr[i]][now[1]+dc[i]] == 1:
                    Q.append((now[0]+dr[i], now[1]+dc[i]))

    if __name__ == "__main__":
        sys.stdin = open("./PS/source/in{}.txt".format(i))
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        cnt = 0
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    BFS(i, j)
                    cnt += 1
        print(cnt)
