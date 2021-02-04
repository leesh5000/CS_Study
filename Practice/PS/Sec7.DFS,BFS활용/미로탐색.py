import sys
from collections import deque
for i in range(1, 2):

    def DFS(r, c):
        global cnt, path
        if r == 6 and c == 6:
            cnt += 1
            print(path)
        else:
            for i in range(4):
                if r+dr[i] < 0 or r+dr[i] > 6 or c+dc[i] < 0 or c+dc[i] > 6:
                    continue
                if board[r+dr[i]][c+dc[i]] == 1:
                    continue
                if check[r+dr[i]][c+dc[i]] == 1:
                    continue
                check[r+dr[i]][c+dc[i]] = 1
                path.append((r+dr[i], c+dc[i]))
                DFS(r+dr[i], c+dc[i])
                check[r+dr[i]][c+dc[i]] = 0
                path.pop()

    if __name__ == "__main__":
        sys.stdin = open('./PS/source/in{}.txt'.format(i), 'r')
        board = [list(map(int, input().split())) for _ in range(7)]
        check = [[0 for _ in range(7)] for _ in range(7)]
        check[0][0] = 1
        cnt = 0
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        path = [(0, 0)]
        DFS(0, 0)
        print(cnt)
