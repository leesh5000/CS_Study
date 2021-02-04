import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(r, c):
        global cnt
        if r == end[0] and c == end[1]:
            cnt += 1
        else:
            for i in range(4):
                if 0 <= r+dr[i] <= n-1 and 0 <= c+dc[i] <= n-1 and check[r+dr[i]][c+dc[i]] == 0:
                    if board[r][c] < board[r+dr[i]][c+dc[i]]:
                        check[r+dr[i]][c+dc[i]] = 1
                        DFS(r+dr[i], c+dc[i])
                        check[r+dr[i]][c+dc[i]] = 0

    if __name__ == "__main__":
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        start = (0, 0)
        end = (n-1, n-1)
        for i in range(n):
            for j in range(n):
                if board[i][j] < board[start[0]][start[1]]:
                    start = i, j
                if board[i][j] > board[end[0]][end[1]]:
                    end = i, j
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        check = [[0 for _ in range(n)] for _ in range(n)]
        check[start[0]][start[1]] = 1
        cnt = 0
        DFS(start[0], start[1])
        print(cnt)
        print(board)
