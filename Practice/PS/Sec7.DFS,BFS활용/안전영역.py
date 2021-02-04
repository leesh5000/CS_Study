from collections import deque
import sys

for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(r, c):
        global check, cnt
        check[r][c] = 0
        for i in range(4):
            if 0 <= r+dr[i] <= n-1 and 0 <= c+dc[i] <= n-1 and check[r+dr[i]][c+dc[i]]:
                DFS(r+dr[i], c+dc[i])

    def BFS(r, c):
        global check, cnt
        Q = deque()
        Q.append((r, c))
        while Q:
            now = Q.popleft()
            check[now[0]][now[1]] = 0
            for i in range(4):
                if 0 <= now[0]+dr[i] <= n-1 and 0 <= now[1]+dc[i] <= n-1 and check[now[0]+dr[i]][now[1]+dc[i]]:
                    Q.append((now[0]+dr[i], now[1]+dc[i]))

    if __name__ == "__main__":
        n = int(input())
        board = [list(map(int, input().split())) for _ in range(n)]
        check = [[1 for _ in range(n)] for _ in range(n)]
        largest = -2147000000
        cnt = 0
        res = []
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(n):
            for j in range(n):
                if largest < board[i][j]:
                    largest = board[i][j]
        for i in range(largest+1):
            cnt = 0
            for j in range(n):
                for k in range(n):
                    if i >= board[j][k]:
                        check[j][k] = 0
                    else:
                        check[j][k] = 1
            # print("%d pre" % i, "\n".join(map(str, check)), sep="\n")
            # print()
            for l in range(n):
                for m in range(n):
                    if check[l][m]:
                        BFS(l, m)
                        cnt += 1
            # print("%d post" % i, "\n".join(map(str, check)), sep="\n")
            # print("count: %d" % cnt)
            # print()
            res.append(cnt)
        print(max(res))
