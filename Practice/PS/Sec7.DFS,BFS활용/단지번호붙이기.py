import sys
for i in range(1, 6):

    def DFS(r, c):
        global cnt
        board[r][c] = 0
        cnt += 1
        for i in range(4):
            if 0 <= r+dr[i] <= n-1 and 0 <= c+dc[i] <= n-1 and board[r+dr[i]][c+dc[i]]:
                DFS(r+dr[i], c+dc[i])

    if __name__ == "__main__":
        sys.stdin = open("./PS/source/in{}.txt".format(i))
        n = int(input())
        board = [list(map(int, input())) for _ in range(n)]

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        cnt = 0
        res = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    DFS(i, j)
                    res.append(cnt)
                    cnt = 0

        res.sort()
        print(len(res))
        print("\n".join(map(str, res)))
        print()
