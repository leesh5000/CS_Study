import sys
for i in range(1, 6):
    sys.setrecursionlimit(10**6)
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(r, c):
        global res
        if r == 10:
            if board[r][c] == 2:
                res = board[r][c]
        else:
            if 0 <= c-1 <= 9 and board[r][c-1] and check[r][c-1] != 1:
                check[r][c-1] = 1
                DFS(r, c-1)
                check[r][c-1] = 0
            elif 0 <= c+1 <= 9 and board[r][c+1] and check[r][c+1] != 1:
                check[r][c+1] = 1
                DFS(r, c+1)
                check[r][c+1] = 0
            else:
                check[r+1][c] = 1
                DFS(r+1, c)
                check[r+1][c] = 0

    if __name__ == "__main__":
        board = [[i for i in range(10)]]
        check = [[0 for _ in range(10)] for _ in range(11)]
        for _ in range(10):
            board.append(list(map(int, input().split())))
        res = 0
        for i in range(10):
            if board[1][i]:
                DFS(1, i)
                if res == 2:
                    print(i)
                    break
